"""Multi-leg route planning through Brumalink cold-storage hubs.

Ported from legacy-route-planner (Java). A single leg may not exceed MAX_LEG_KM, which keeps
every leg within one driver shift and the passive-cooling autonomy of our containers.
"""

import heapq
import math

MAX_LEG_KM = 450.0

HUBS: dict[str, tuple[float, float]] = {
    "WAW": (52.2297, 21.0122),  # Warsaw
    "POZ": (52.4064, 16.9252),  # Poznan
    "WRO": (51.1079, 17.0385),  # Wroclaw
    "KRK": (50.0647, 19.9450),  # Krakow
    "GDN": (54.3520, 18.6466),  # Gdansk
    "BER": (52.5200, 13.4050),  # Berlin
    "PRG": (50.0755, 14.4378),  # Prague
    "VIE": (48.2082, 16.3738),  # Vienna
    "BUD": (47.4979, 19.0402),  # Budapest
}


def distance_km(a: str, b: str) -> float:
    (lat1, lon1), (lat2, lon2) = HUBS[a], HUBS[b]
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0 * math.asin(math.sqrt(h))


def plan_route(origin: str, destination: str, max_leg_km: float = MAX_LEG_KM) -> list[str]:
    """Shortest hub-to-hub route (Dijkstra) where no leg is longer than max_leg_km."""
    for hub in (origin, destination):
        if hub not in HUBS:
            raise ValueError(f"Unknown hub: {hub!r}")

    best = {origin: 0.0}
    previous: dict[str, str] = {}
    queue = [(0.0, origin)]
    while queue:
        dist, hub = heapq.heappop(queue)
        if hub == destination:
            break
        if dist > best[hub]:
            continue
        for nxt in HUBS:
            leg = distance_km(hub, nxt)
            if nxt == hub or leg > max_leg_km:
                continue
            if dist + leg < best.get(nxt, math.inf):
                best[nxt] = dist + leg
                previous[nxt] = hub
                heapq.heappush(queue, (dist + leg, nxt))

    if destination not in best:
        raise ValueError(f"No route from {origin} to {destination} within {max_leg_km} km legs")
    route = [destination]
    while route[-1] != origin:
        route.append(previous[route[-1]])
    return route[::-1]
