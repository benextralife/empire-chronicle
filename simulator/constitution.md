# Constitution of the Kingdom of Ashworth
*Version 1.0 — Core Rules Layer*

---

## Preamble

This Constitution defines the immutable laws of the Kingdom of Ashworth simulation. All engines, behaviors, and world states must conform to these rules. No exception.

---

## Article I: Agents

1. Every agent is a unique citizen with:
   - **Name**: immutable once born
   - **Age**: increases with time; death threshold randomized
   - **Health**: 0–100; death at 0
   - **Wealth**: non-negative; income/expense per tick
   - **Faction**: one of {Crown, Merchant Guild, Academy, Shadow Market}
   - **Personality**: five dimensions, each 0.0–1.0
   - **Skills**: {business, engineering, negotiation, research}, each 0–100
   - **Memory**: last 20 interactions stored locally
   - **Alive**: boolean; once false, irreversible

2. Agent death occurs when:
   - health ≤ 0 from disease/accident/old age
   - age exceeds natural lifespan (80 + random 30)
   - mass-mortality event strikes with probability roll

3. Agent birth occurs when:
   - alive population falls below threshold (8)
   - birth probability roll succeeds

---

## Article II: Factions

1. Four factions exist:
   - **Crown** (Government): blue, policy power
   - **Merchant Guild** (Economy): green, trade focus
   - **Academy** (Research): purple, knowledge focus
   - **Shadow Market** (Black market): red, illicit trade

2. Factions compete for territory on the 8×8 grid.

3. Faction strength = alive member count + controlled territory count.

4. Faction territory can be contested (conflict state) or peaceful.

---

## Article III: Resources

1. Six resources: Money, Food, Materials, Energy, Influence, Population.

2. Resources fluctuate per tick with bounded random walk.

3. Minimum resource floor: 1,000.

4. Population = count of alive agents.

---

## Article IV: Economy

1. GDP is the sum of all faction productivity.

2. Inflation fluctuates ±0.5% per tick, clamped to [-2%, +15%].

3. Market trend cycles through: stable → growing → shrinking → volatile.

4. Unemployment inversely correlated with GDP growth.

---

## Article V: Events

1. Events are generated each tick with probability P(event) = 35%.

2. Events are weighted by severity (w: 1–4).

3. Event categories: infrastructure, trade, policy, research, health, disaster, birth, death, epidemic.

4. Events modify:
   - agent mood
   - resource levels
   - faction relationships
   - territory control

---

## Article VI: Territory

1. The Kingdom is an 8×8 grid (64 zones).

2. Each zone has: owner (faction id or null), contested (boolean).

3. Territory can change hands through:
   - random faction expansion
   - player intervention
   - conflict events

4. Contested zones pulse visually and cannot be peacefully used.

---

## Article VII: Time

1. One tick = 10 simulated minutes.

2. 6 ticks = 1 simulated hour.
   24 hours = 1 day.

3. Agent age accumulates: +0.007 years per tick.

4. Health decay probability: 1% per tick of -2 to -8 HP.

---

## Article VIII: Social Dynamics

1. Trust increases through cooperation events.
2. Distrust increases through conflict events.
3. Betrayal creates long-term hostility (stored in agent memory).
4. Shared goals create temporary alliances.
5. Proximity increases interaction frequency (same zone = +20% interaction chance).

---

## Article IX: Player Intervention

1. Visitors may click territory cells to claim/release.
2. Visitors may trigger random events.
3. Visitors may pause/speed/reset the world.
4. Player actions are logged with tick timestamp.

---

## Article X: Consistency

1. All random operations use `Math.random()` seeded by browser clock.
2. State is persisted to `localStorage` every tick.
3. Archives are written every 6 ticks (1 simulated hour).
4. No external network calls; fully offline-capable.

---

*End of Constitution*
