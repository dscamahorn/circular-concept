# Circular Prototype RAG Registry

**Version:** 0.0
**Purpose:** Structured knowledge base for generating circular economy business model prototypes from an organization profile and a stated outcome.
**Source frameworks:** Sitra/Deloitte Circular Economy Playbook, Disrupt Design Circular Economy Workshop Kit, Circular Systems Design Handbook, Board of Innovation Circular Economy Report, Circular Prototype Prompter (Scamahorn)

---

## How to Use This Registry

This registry is the single source of truth for a Concept Generator producing circular model prototypes. When given an **Organization Profile** and a **Desired Outcome**, the generator must:

1. Read the full Organization Profile (Fields 1-6 below).
2. Identify which value chain inefficiencies are present using the Inefficiency Taxonomy.
3. Match those inefficiencies to one or more Prototype-Ready Circular Mechanics.
4. Generate 3-5 distinct prototype concepts, each in the required Concept Output Format.
5. Run the Prototype-Readiness Heuristic Test on every concept before surfacing it.
6. Apply the Validation Rubric to confirm circular integrity.
7. Return only concepts that pass both the heuristic test and the rubric.

Do not surface a concept that cannot pass Step 5. If a concept fails the heuristic, it is a design principle, not a prototype. Pair it with a named mechanic from Section 3 and try again, or discard it.

---

## Section 1: Organization Profile Schema

A facilitator or user completes these fields once. Every concept generated must be traceable back to at least one field in this profile.

| Field | Label | What to Capture |
|---|---|---|
| **1** | What does the organization make or do? | Industry, product or service, rough scale. One sentence. |
| **2** | Where does waste, inefficiency, or end-of-life live in their value chain? | What gets thrown away, returned, unused, or undervalued today. |
| **3** | What pressure is driving the need to change? | Regulatory deadline, investor commitment, competitor move, or internal mandate. |
| **4** | What circular territory have they already explored? | Initiatives underway, models already considered, or directions already ruled out. Prevents retreading covered ground. |
| **5** | What does a successful outcome look like for them? | New revenue, cost reduction, compliance, brand differentiation. Anchors both generation and validation. |
| **6** *(optional)* | What capabilities does the organization still need to develop? | Useful for scoping concepts to what is feasible now vs. aspirational. Acts as a feasibility filter. |

> **Registry instruction:** Field 5 is the primary anchor for concept relevance. Field 4 is the exclusion filter. If a generated concept closely resembles something in Field 4, discard it and generate a replacement.

---

## Section 2: Value Chain Inefficiency Taxonomy

Use this taxonomy to translate Field 2 of the profile into a diagnostic category. Every concept must address at least one of these inefficiencies -- not merely acknowledge it.

| Inefficiency Type | Description | Circular Signal |
|---|---|---|
| **Unsustainable material use** | Virgin materials consumed with no recovery pathway | Closed-loop material flows, bio-based inputs, industrial symbiosis |
| **Underused capacity** | Products, assets, or infrastructure sitting idle | Sharing platforms, pay-per-use, peer access models |
| **Short product lifetime** | Products discarded before end of functional life | Repair-as-a-service, remanufacturing, design for modularity |
| **Wasted end-of-life value** | Products landfilled or incinerated rather than recovered | Take-back programs, deposit-return, resale marketplaces |
| **Missed customer relationship value** | Revenue limited to a single transaction rather than ongoing engagement | Product-as-a-service, performance-as-a-service, subscription access |
| **Toxic or non-recoverable material content** | Product design locks in materials that cannot circulate | Total product redesign, design for disassembly, low-impact material substitution |
| **Waste-stream volume with no destination** | Byproducts or offcuts accumulate without a receiving system | Industrial symbiosis, waste-as-resource partnerships |

---

## Section 3: Prototype-Ready Circular Mechanics

These are the mechanics the Concept Generator must draw from. Each has a crisp, nameable label, a visible user interaction, and a clear value exchange -- making them immediately expressible as a testable prototype without further expert interpretation.

Only these mechanics qualify as prototype-ready. Design principles (e.g., "design for durability," "full life cycle thinking") are upstream framing, not interaction-level mechanics. They must be coupled with a mechanic from this table before a concept can be surfaced.

| Mechanic | User Interaction | Value Exchange | Closes Which Loop |
|---|---|---|---|
| **Deposit-return** | User pays a deposit at purchase, gets it back on return | Financial incentive drives return behavior; the loop is the value | Material recovery loop |
| **Product as a service (PaaS)** | User pays to access, not own; producer retains the asset | Ongoing revenue replaces one-time sale; producer controls end-of-life | Asset retention loop |
| **Performance as a service** | User pays for an outcome (lumens, not lightbulbs); supplier absorbs product risk | Outcome billing aligns producer incentives with efficiency and longevity | Resource efficiency loop |
| **Remanufacturing** | Producer takes back, restores to original spec, and re-sells at a lower price point | Secondary revenue from refurbished asset; lower-cost entry point for buyers | Technical material loop |
| **Repair as a service** | Producer or third party extends product life through paid servicing | Extended product life generates service revenue; defers replacement cost for user | Product lifespan loop |
| **Take-back / gamified returns** | User returns end-of-life product in exchange for credit, discount, or reward | Behavioral incentive closes the return gap; recovered material re-enters supply chain | Material recovery loop |
| **Sharing platform** | Users access idle assets without owning them; platform captures the transaction | Idle asset utilization converted to revenue; user avoids ownership cost | Utilization loop |
| **Pay-per-use** | User pays only for consumption; removes the ownership burden | Usage-based pricing aligns cost with value; producer retains and manages the asset | Asset retention and utilization loop |
| **Resale / second-hand marketplace** | Producer or platform brokers the product's second life | Extended revenue from the same unit; lower-cost access for secondary buyers | Product lifespan loop |
| **Waste-as-resource (industrial symbiosis)** | One organization's waste stream becomes another's input material | Waste disposal cost eliminated for sender; input cost reduced for receiver | Industrial material loop |

### Extended Design Strategy Reference

The following strategies from the Disrupt Design Circular Economy framework are **upstream design enablers**, not standalone prototype mechanics. Use them to qualify or sharpen a concept that already has a named mechanic -- not as replacements for one.

- Closed loop business model / closed loop production model
- Design for disassembly, remanufacture, repair, modularity, recyclability, durability, multifunctionality, dematerialization
- Producer stewardship / extended producer responsibility
- Full life cycle thinking
- Total product redesign / functionality reassessment
- High value recycling / on-site composting / infrastructure development
- Low impact materials

---

## Section 4: Concept Output Format

Every concept surfaced must conform to this structure. Incomplete output is not acceptable.

```
### Concept [N]: [Descriptive Title]

**Circular mechanic:** [Name from Section 3 mechanic table]
**Target user:** [Who performs the interaction -- be specific, not generic]
**Value chain inefficiency addressed:** [Category from Section 2 taxonomy]
**Pressure addressed:** [Reference to Field 3 of the Organization Profile]

**Concept description:**
[2-4 sentences. Describe the interaction, the value exchange, and how the loop closes.
Name the mechanic explicitly. Do not use passive voice or vague language like "could potentially"
or "might help." State what happens, who does it, and what they get.]

**Prototype-readiness sentence:**
"The user [does X], and in return [gets Y], while the producer [closes Z loop]."

**Prototype-readiness verdict:** PASS / FAIL
[If FAIL: state which element is missing and whether the concept can be salvaged
by pairing it with a named mechanic.]

**Outcome alignment:** [1 sentence connecting this concept to Field 5 of the profile]

**Feasibility flag (if Field 6 is populated):**
[1 sentence on whether this concept is within current capability or aspirational]
```

---

## Section 5: Prototype-Readiness Heuristic Test

This test is mandatory. Run it on every concept before including it in output. A concept that cannot complete the sentence is a design principle, not a prototype. It must either be paired with a named mechanic from Section 3 or discarded.

### The Heuristic Sentence

> *"The user [does X], and in return [gets Y], while the producer [closes Z loop]."*

### Completing the Sentence: Rules

Each bracket must be filled with a specific, observable element:

| Bracket | What it requires | Failing examples | Passing examples |
|---|---|---|---|
| **[does X]** | A concrete, nameable user action | "engages with the system," "participates in sustainability" | "returns the container at checkout," "books a device through the app" |
| **[gets Y]** | A tangible, specific return of value | "benefits from circularity," "contributes to a better future" | "receives a $5 loyalty credit," "accesses the equipment for the shift at no upfront cost" |
| **[closes Z loop]** | A named material, product, or value loop | "improves sustainability," "reduces waste" | "closes the glass material loop," "retains the asset and controls refurbishment" |

### Verdict Logic

- **PASS:** All three brackets are filled with specific, observable elements. Surface the concept.
- **FAIL - Salvageable:** One bracket is vague or missing. The concept has a viable mechanic but needs sharpening. Revise the description and re-run the test once.
- **FAIL - Discard:** Two or more brackets cannot be completed. The idea is at the design principle level. Do not surface it. Note it as a direction for future development if relevant.

---

## Section 6: Validation Rubric

After passing the heuristic test, every concept must be screened against these criteria. A concept that fails more than one criterion is not circular -- it is incremental or greenwashed.

| Criterion | Question | What failure looks like |
|---|---|---|
| **Loop closure** | Does the concept close a material or resource loop rather than slow its disposal? | Recycling with no confirmed receiving system; offsetting rather than redesigning |
| **Named mechanic** | Is the circular mechanic explicit and named from the Section 3 table? | Vague references to "sustainability practices" or "eco-friendly initiatives" |
| **Interaction clarity** | Does the concept identify a plausible user, a specific interaction, and a clear value exchange? | No identifiable user; no moment of transaction or behavior change |
| **Structural change** | Is the concept free from greenwashing -- does it require structural change, not just incremental improvement? | Lighter packaging, marginal efficiency gains, voluntary offsetting programs |
| **Profile relevance** | Is the concept relevant to the organization's industry, pressure, and stated success criteria? | Generic circular concepts that could apply to any organization |
| **Prototype testability** | Could the concept be expressed as a testable prototype without further expert input? | Concepts requiring years of R&D, undefined infrastructure, or unrealized partnerships |
| **Non-duplication** | Is the concept meaningfully different from circular territory already explored (Field 4)? | Direct overlap with initiatives already underway or already ruled out |

---

## Section 7: Circularity Principles Reference (Design Guardrails)

These principles, drawn from the Circular Systems Design Handbook and Sitra/Deloitte Playbook, inform what "circular" means at the system level. Use them to pressure-test concepts for depth. They are not mechanics -- they are the "why" behind every mechanic.

- **Waste equals food:** All material outputs are nutrients to another part of the system.
- **Life cycle thinking:** Value is designed to be captured across the entire product life, not just at point of sale.
- **Extended producer responsibility:** The producer retains accountability for the product through end-of-life.
- **Product-service systems:** The shift from selling products to delivering outcomes through long-term relationships.
- **True cost accounting:** Environmental and social impacts are internalized, not externalized.
- **Industrial ecology:** Industrial systems are modeled on ecological nutrient cycles, not linear extraction flows.
- **Cradle to cradle:** End-of-life is designed at the conception stage, not addressed after the fact.

---

## Section 8: Circular KPI Reference

Use this section to give concepts measurable anchors when Field 5 names a specific business outcome. Selecting relevant KPIs strengthens the outcome alignment statement in the concept output.

| Outcome Type              | Relevant KPIs                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Revenue growth**        | % increase in service/resale revenue, secondary market value captured per unit, number of repair transactions                  |
| **Cost reduction**        | % reduction in virgin material input, cost per unit recovered, reduction in waste-to-landfill cost                             |
| **Regulatory compliance** | % recycled content in product, % products designed with end-of-life pathway, compliance rate with applicable regulation        |
| **Brand differentiation** | NPS on circular service offering, % customers engaging with take-back or repair program, media coverage of circular initiative |
| **Asset performance**     | Product utilization rate (%), product lifetime (years), idle time reduction (%)                                                |
| **Loop closure**          | % products captured as feedstock, kg of material recovered per cycle, % of installed base with known end-of-life destination   |

---

## Section 9: Sample Concept (Reference Output)

Use this as the quality benchmark for generated output. Every concept produced should be at this level of specificity.

**Organization profile input:**
> A mid-size cosmetics brand manufacturing single-use plastic packaging at scale, facing an EU regulatory deadline requiring 30% recycled content in all packaging by 2027, with no existing take-back or end-of-life program. A successful outcome would demonstrate regulatory compliance while opening a new revenue stream.

---

### Sample Concept: Deposit-Return Remanufacturing Partnership

**Circular mechanic:** Deposit-return + Remanufacturing
**Target user:** Retail cosmetics customer returning empty containers at point of purchase
**Value chain inefficiency addressed:** Wasted end-of-life value
**Pressure addressed:** EU 30% recycled content regulatory deadline (2027)

**Concept description:**
The brand registers as an official partner with municipal cosmetics packaging collection infrastructure in Germany and the Netherlands, currently underutilized and seeking brand partners. At checkout, customers pay a small deposit on packaging. On their next visit, they return empty containers and receive a loyalty credit redeemable immediately. Returned containers are sorted, cleaned, and reprocessed into certified recycled input material -- closing the loop within the industry and meeting the 2027 recycled content threshold. Certified recycled material is sold to packaging suppliers as a secondary revenue stream.

**Prototype-readiness sentence:**
"The user returns empty containers at the point of purchase, and in return receives a loyalty credit, while the producer closes the plastic packaging loop and generates certified recycled material revenue."

**Prototype-readiness verdict:** PASS

**Outcome alignment:** Directly addresses the 2027 compliance deadline while creating a new material revenue stream from certified recycled content -- satisfying both dimensions of Field 5.

**Feasibility flag:** Requires partnership with existing collection infrastructure (available), not greenfield build. Feasible within a 12-month pilot window.

---

## Section 10: Registry Metadata

| Field | Value |
|---|---|
| **Primary source frameworks** | Sitra/Deloitte Circular Economy Playbook; Disrupt Design Circular Economy Workshop Kit; Circular Systems Design Handbook (Acaroglu); Board of Innovation Circular Economy Report; Circular Prototype Prompter (Scamahorn) |
| **Mechanics table version** | 1.0 -- 10 prototype-ready mechanics |
| **Heuristic version** | 1.0 -- three-bracket sentence test |
| **Intended generator role** | Concept Generator agent in a three-agent system (Signal Monitor > Concept Generator > Circular Validator) |
| **Output target** | 3-5 distinct, principle-compliant circular prototype concepts per organization profile |
| **Quality bar** | Each concept must pass the Prototype-Readiness Heuristic Test (Section 5) and the Validation Rubric (Section 6) before surfacing |
| **Exclusion logic** | Concepts overlapping with Field 4 (explored territory) are discarded and replaced |
| **Greenwash guard** | Any concept relying on incremental improvement, voluntary offsetting, or efficiency gains without loop closure fails the Validation Rubric |

---

## Section 11: RAG Entry Field Taxonomy (Controlled Vocabulary)

This section is the canonical source for classification field definitions used across all RAG knowledge base files. Update definitions here only. RAG files reference this section rather than duplicating it.

---

### G -- Circular Business Model (Primary)

The top-level strategic pattern the case exemplifies. Each entry carries exactly one primary model.

| Value | Definition |
|---|---|
| **Circular Inputs** | Products made from recycled, renewable, or bio-based materials that eliminate the use of virgin or toxic inputs. Includes circular supplies and sustainable product design strategies. |
| **Sharing Platform** | A platform or system that enables users to share, rent, or access products or assets rather than own them outright, increasing utilization rates across the user base. |
| **Product as a Service** | The producer retains ownership of the product and charges customers for the service or performance it delivers (e.g., per use, per outcome, or subscription), creating a financial incentive for durability, efficiency, and end-of-life recovery. |
| **Product Use Extension** | Business models that keep products and components in use for longer through repair, remanufacturing, refurbishment, resale, or upgrading, deferring or avoiding end of life. |
| **Resource Recovery** | Systems that recover energy, materials, or nutrients from products or waste streams at end of life, through recycling, upcycling, anaerobic digestion, composting, or industrial symbiosis. |

---

### H -- Circular Sub-Models

One or more sub-models that describe the specific circular mechanisms deployed within the primary model. Entries may carry multiple values.

| Value | Definition |
|---|---|
| **Circular supplies** | Sourcing inputs that are recycled, renewable, or bio-based, replacing virgin or hazardous materials. |
| **Sustainable product design** | Designing products to use fewer materials, last longer, be safer, or be more easily repaired, disassembled, or recycled. |
| **Share** | Enabling multiple users to access the same physical asset sequentially or simultaneously, peer-to-peer or platform-mediated. |
| **Pay-per-use** | Charging customers only for the units of service or output they actually consume rather than for ownership of the product. |
| **Performance as a service** | Charging for a guaranteed outcome or level of service, such as lux of light or degrees of cooling -- outcome-based pricing. |
| **Repair and maintain** | Servicing and fixing products to restore function and extend useful life, avoiding premature replacement. |
| **Upgrade** | Improving a product's capability or appearance to extend its relevance and life, avoiding full replacement. |
| **Remanufacture** | Restoring a used product or component to original specification, typically via disassembly, cleaning, inspection, replacement of worn parts, and testing. |
| **Resell** | Selling a product for a second or subsequent time to a new owner through a secondary market, second-hand or pre-owned. |
| **Return** | Bringing nutrients or materials back to the biological or technical cycle after use, through composting, recycling, or soil amendment. |
| **Recycle / upcycle** | Processing end-of-life materials into new raw material inputs, ideally at equal or higher quality (upcycling) rather than lower quality (downcycling). |
| **Take-back / gamified returns** | Manufacturer or retailer-operated programs that collect used products or packaging from customers, often with an incentive such as a discount, deposit, or loyalty points. |
| **Waste-as-resource (industrial symbiosis)** | One company's waste or by-product becomes a productive input for another company, eliminating disposal and replacing virgin material. |
| **Product as a service** | The producer retains ownership; the customer pays for access or use. (Sub-model variant -- see also G definition.) |

---

### AC -- Inefficiency Type

The underlying linear economy failure the circular model addresses. Entries may carry multiple values.

| Value | Definition |
|---|---|
| **Wasted end-of-life value** | Valuable materials, components, or nutrients are lost at end of product or material life, through landfill, incineration, or unrecovered disposal. |
| **Unsustainable materials** | Products or processes rely on virgin, toxic, non-renewable, or ecologically harmful inputs that deplete natural systems. |
| **Premature product life** | Products are discarded or replaced before their functional life is exhausted, due to design, fashion cycles, or lack of repair options. |
| **Underutilised capacity** | Physical assets (products, equipment, space, vehicles) sit idle for a significant portion of their potential productive life. |
| **Unexploited customer engagement** | Existing customer relationships or touchpoints are not used to create circular value, such as no take-back program, no service model, or no loyalty loop. |

---

### AD -- Economic / Regulatory Pressure

The primary external or internal driver that motivated the circular initiative. Entries may carry multiple values.

| Value | Definition |
|---|---|
| **Internal mandate or leadership commitment** | A founder's mission, CEO commitment, or board-level strategic decision drove the circular initiative, not primarily external pressure. |
| **Consumer demand shift** | Changing customer preferences, values, or purchasing behavior toward sustainable, ethical, or low-waste options created market pull. |
| **Regulatory / compliance pressure** | Existing or anticipated legislation, standards, or policy requirements made the circular model necessary or commercially advantageous. |
| **Investor or ESG pressure** | Institutional investors, ESG ratings, sustainability disclosure requirements, or capital market expectations drove the circular transition. |
| **Competitor or market pressure** | Competitive dynamics, such as rivals launching circular models, new market entrants, or shifting industry norms, prompted the circular response. |
| **Resource cost or scarcity** | Rising costs, supply volatility, or strategic scarcity of virgin materials, energy, or water made circular inputs or efficiency economically attractive. |

---

### AE -- Success Criteria

The primary metric or outcome against which the circular initiative is evaluated. Entries may carry multiple values.

| Value | Definition |
|---|---|
| **Cost reduction** | The circular model reduces input costs, waste disposal costs, energy costs, or total cost of ownership for the organization or its customers. |
| **New revenue or market access** | The circular model opens a new revenue stream, customer segment, or market that the linear model could not access. |
| **Customer retention or deepened relationship** | The circular model creates a longer-term or more frequent relationship with customers, through service contracts, take-back, subscription, or loyalty. |
| **Brand differentiation** | The circular model creates a distinct, credible sustainability positioning that differentiates the organization from linear competitors. |
| **Regulatory compliance** | The circular model enables the organization to meet existing or anticipated legal, policy, or reporting requirements. |
| **Supply chain resilience** | The circular model reduces dependency on volatile, scarce, or geopolitically risky virgin material inputs by closing material loops internally or locally. |
| **Emissions or resource reduction target** | The circular model is primarily evaluated against a quantified environmental goal, such as carbon, waste, water, or material reduction, rather than a financial metric. |

---

### AH -- Prototype Readiness Statement (Classification)

Indicates how fully the case supports a user-facing circular prototype. Used to assess which entries can be directly adapted for concept generation.

| Value | Definition |
|---|---|
| **Prototype-ready (complete sentence)** | A complete sentence following the pattern: "The user [does X], and in return receives [Y], while the producer closes the [loop name] loop by [doing Z]." All three elements are present and specific enough to prototype a user interaction. |
| **Mechanic present but not prototype-ready** | The circular mechanic is identifiable (e.g., take-back exists, service model exists) but the case lacks sufficient detail on the user interaction, incentive structure, or return exchange to draft a complete prototype sentence. |
| **Design principle only** | The case describes a design philosophy, material choice, or policy framework rather than a discrete product-user interaction. No testable circular exchange between a user and a producer is described. Applies to most policy/governance cases, research projects, and supply-chain-only interventions. |

---

### AM -- Maturity Stage

The lifecycle stage of the circular initiative at the time of documentation. Each entry carries exactly one value.

| Value | Definition |
|---|---|
| **Pilot** | Model under active testing at limited scale; not yet commercially launched or self-sustaining. |
| **Early Growth** | Past initial validation; generating early commercial activity but not yet established at scale. |
| **Growth** | Commercially active, scaling, and generating revenue; not yet at full national or sector-wide scale. |
| **Operating at scale** | Mature system operating at full commercial, national, or sector-wide scale with proven unit economics. |

---

## Section 12: RAG File Usage Guidance (Shared)

This section is the canonical source for retrieval and prototyping guidance shared across all RAG knowledge base files. RAG files reference this section rather than duplicating it.

### How to Use a RAG File

- **Matching:** Retrieve entries by `circular_model_primary`, `topic_tags`, `geography`, `org_profile`, or `loop_type_emf` to find analogues for a target organization.
- **Prototyping:** Feed the `prototype_readiness_statement` field directly into a concept generation prompt as a "how it works" template.
- **Gap analysis:** Use `barriers_challenges` and `capability_requirements` to surface prerequisites and risk factors for similar organizations.
- **Regulatory alignment:** Cross-reference `regulatory_policy_enabler` and `economic_regulatory_pressure` to assess policy tailwinds in a target market.

### Prompt Matching Guidance

When retrieving entries for prototype generation, prioritize matching on:

1. `circular_model_primary` -- the broadest strategic pattern (Circular Inputs vs. Sharing Platform vs. Resource Recovery)
2. `org_profile` -- org size and type (SME vs. large enterprise; B2B vs. B2C vs. B2B2C)
3. `value_chain_stage` -- where in the chain the target organization operates
4. `inefficiency_type` -- what waste or underperformance the prototype must address
5. `geography` -- for regulatory and cultural context alignment

Individual RAG files may define additional domain-specific priorities beyond these five.

### Prototype Generation Template

Use the following structure when generating a concept prototype from a retrieved entry:

```
ANALOGOUS CASE: [id] -- [title]
ORGANIZATION MATCH: [why the org profile is analogous]
CIRCULAR LOOP PATTERN: [circular_model_primary] via [circular_sub_models]
HOW IT WORKS: [prototype_readiness_statement adapted to target org]
KEY CAPABILITIES REQUIRED: [capability_requirements]
KNOWN BARRIERS: [barriers_challenges]
REGULATORY TAILWIND: [regulatory_policy_enabler adapted to target market]
SUCCESS METRIC ANALOGY: [quantified_impact adapted to target scale]
```

### Confidence and Data Quality

All entries in RAG knowledge base files carry a `confidence_score` of **High**, sourced directly from the Ellen MacArthur Foundation circular examples database. Field values marked "Not stated" in the source have been omitted rather than interpolated. Do not treat omitted fields as negative evidence -- they reflect source limitations, not model failure.
