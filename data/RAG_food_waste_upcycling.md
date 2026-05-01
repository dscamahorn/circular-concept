---
rag_id: food-waste-upcycling
rag_version: "1.0"
created: 2026-04-21
source_file: food-waste-upcycling.csv
source_domain: Ellen MacArthur Foundation Circular Economy Examples
topic_domain: Food Waste Upcycling
related_files:
  - path: circular_prototype_rag_registry.md
    role: clarifier
    description: Additional context and guidance for interpreting RAG entries
use_case: Retrieval-Augmented Generation knowledge base for generating circular economy concept prototypes. Use these entries to match organization profiles against proven food waste upcycling models, extract analogous strategies, and scaffold new circular business model concepts for similar sectors, geographies, and maturity stages.
schema_version: "1.1"
total_entries: 5
confidence_filter: High
entry_id_prefix: FWU
fields:
  - id
  - title
  - url
  - org_name
  - org_one_liner
  - description
  - topic_tags
  - material_resource_loop
  - circular_model_primary
  - circular_sub_models
  - loop_type_emf
  - value_chain_stage
  - linear_model_replaced
  - org_profile
  - founding_maturity
  - geography
  - revenue_model
  - pricing_mechanism
  - technology_enabler
  - target_users
  - value_propositions
  - partnerships
  - quantified_impact
  - regulatory_policy_enabler
  - barriers_challenges
  - replication_model
  - confidence_score
  - inefficiency_type
  - economic_regulatory_pressure
  - success_criteria
  - circular_maturity_prior
  - capability_requirements
  - prototype_readiness_statement
retrieval_tags:
  - food-waste
  - upcycling
  - surplus-food
  - by-product-valorisation
  - waste-as-resource
  - agricultural-waste
  - urban-organics
  - fermentation
  - alternative-protein
  - subscription-model
  - B2B
  - B2C
  - B2B2C
  - food-and-beverage
  - plastics
  - EPR
  - circular-inputs
  - sharing-platform
  - resource-recovery
  - circular-inputs
  - biological-cycle
  - industrial-symbiosis
  - SME
  - startup
  - Netherlands
  - UK
  - USA
  - regenerative-agriculture
  - open-source
  - transparency
---

# Food Waste Upcycling -- Circular Economy RAG Knowledge Base

## Purpose

This file is a structured, retrievable knowledge base of real-world circular
economy case studies focused on food waste upcycling. Each entry captures
a verified example drawn from the Ellen MacArthur Foundation circular examples
library. Entries are formatted for RAG (Retrieval-Augmented Generation) use:
each record is self-contained, richly tagged, and includes a prototype
readiness statement suitable for direct use in concept generation prompts.

## How to Use This File

- **Matching:** Retrieve entries by `circular_model_primary`, `topic_tags`,
  `geography`, `org_profile`, or `loop_type_emf` to find analogues for a
  target organization.
- **Prototyping:** Feed the `prototype_readiness_statement` field directly into
  a concept generation prompt as a "how it works" template.
- **Gap analysis:** Use `barriers_challenges` and `capability_requirements`
  to surface prerequisites and risk factors for similar organizations.
- **Regulatory alignment:** Cross-reference `regulatory_policy_enabler` and
  `economic_regulatory_pressure` to assess policy tailwinds in a target market.

---

## Entries

---

### FWU-001

**id:** FWU-001
**title:** Brewing Beer from Surplus Bread
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/brewing-beer-from-surplus-bread
**confidence_score:** High

#### Organization

**org_name:** Toast Ale
**org_one_liner:** Toast Ale is a UK craft beer company that replaces approximately one-third of the malted grain in its brewing process with surplus bread collected from bakeries and food businesses, donating all profits to food waste charities.
**org_profile:** Size: SME | Industry: Food & Beverage / Craft Beer | Type: B2C
**founding_maturity:** Founded 2016 | Maturity: Growth
**geography:** United Kingdom (primary); international licensing partnerships

#### Description

Toast Ale replaces approximately one-third of the malted grain in its brewing
process with surplus bread collected from bakeries and food businesses. By
upcycling a high-volume food waste stream -- 44% of all bread in the UK is
wasted -- into a premium craft beer ingredient, Toast Ale creates commercial
value from waste while reducing the agricultural land, water, and energy needed
for conventional malted grain production. The company shares its recipe openly
to encourage replication and donates 100% of profits to Feedback, a food waste
charity campaigning for systemic change. The open-source recipe model allows
other breweries globally to adopt the same process without licensing fees,
amplifying environmental impact beyond Toast Ale's own production volume.

#### Classification

**topic_tags:** Food & Agriculture, Business
**circular_model_primary:** Resource Recovery
**circular_sub_models:** Waste-as-resource (industrial symbiosis), Recycle / upcycle, Circular supplies
**loop_type_emf:** Biological cycle
**value_chain_stage:** Production, End of Life, Cross-stage
**material_resource_loop:** Surplus bread from bakeries and food businesses replaces approximately one-third of malted grain in beer brewing -- biological waste-to-value loop

#### Linear Model Replaced

Surplus bread sent to landfill or anaerobic digestion with no commercial value
recovered, while breweries continue to source 100% virgin malted grain as a
production input.

**inefficiency_type:** Wasted end-of-life value, Unsustainable materials

#### Business Model

**revenue_model:** Product sales (craft beer sold via retail and online channels); licensing of open-source recipe to partner breweries; 100% of profit donated to food waste charity
**pricing_mechanism:** Premium product pricing (craft beer positioning)
**technology_enabler:** Standard brewing infrastructure adapted for bread-based grain substitution; open-source recipe documentation enabling replication

#### Users and Partners

**target_users:** Primary: UK and international craft beer consumers. Secondary: Bakeries and food businesses supplying surplus bread; independent breweries adopting the open-source recipe
**value_propositions:** Consumers: premium craft beer with a transparent food-waste-reduction story. Bakeries: a dignified, commercial-channel alternative to waste disposal. Partner breweries: a ready-made circular supply chain model with no IP barrier.
**partnerships:** Feedback (food waste charity and profit recipient); bakery supply partners; international brewery licensees

#### Impact and Context

**quantified_impact:** 44% of UK bread is wasted; Toast Ale's model diverts surplus bread into a premium commercial ingredient, replacing a portion of virgin malted grain and reducing associated land, water, and energy use. Recipe shared openly to maximize replication impact.
**regulatory_policy_enabler:** UK food waste reduction targets; Courtauld Commitment voluntary framework; general EU and UK sustainability reporting expectations create commercial incentive for suppliers to demonstrate waste diversion.
**barriers_challenges:** Consistent supply of quality surplus bread; maintaining food-safety certification for upcycled inputs; consumer education on upcycled-ingredient products; scaling collection logistics as production grows.
**replication_model:** Open-source recipe sharing actively encourages direct replication by any brewery globally; no licensing fee or exclusivity barrier.

#### Prototype Readiness

**circular_maturity_prior:** Low (most craft breweries source 100% virgin malt with no waste-input integration)
**capability_requirements:** Relationships with local bakeries or food businesses for reliable surplus bread supply; food-safety certification for upcycled grain substitutes; basic supply chain adaptation within existing brewing infrastructure; brand storytelling capability around waste provenance.
**economic_regulatory_pressure:** Consumer demand shift; internal mandate or leadership commitment; regulatory / compliance pressure (food waste targets)
**success_criteria:** Emissions or resource reduction target; brand differentiation; new revenue or market access
**prototype_readiness_statement:** A bakery or food business identifies surplus bread as a reliable by-product stream and partners with a local craft brewery to supply it as a malted grain substitute; the brewery produces a co-branded beer that carries the surplus-bread story on pack; both parties share the waste-diversion metric in their sustainability reporting, and the brewery optionally adopts the open-source Toast Ale recipe to reduce development costs and time to market.

---

### FWU-002

**id:** FWU-002
**title:** Radical Transparency in Collaborations to Eradicate Food Waste
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/radical-transparency-in-collaborations-to-eradicate-food-waste-rescued
**confidence_score:** High

#### Organization

**org_name:** Rescued
**org_one_liner:** Rescued is a UK food company that sources surplus and cosmetically rejected food from farmers and sells it to consumers via a subscription box model, applying radical transparency to disclose the exact origin and reason for surplus of every product.
**org_profile:** Size: SME / Startup | Industry: Food & Agriculture / Direct-to-Consumer | Type: B2C
**founding_maturity:** Early growth | Maturity: Growth
**geography:** United Kingdom

#### Description

Rescued sources surplus and rejected food from farmers and producers -- produce
discarded due to cosmetic imperfection, overproduction, or market rejection --
and sells it directly to consumers through a subscription box model. The company
applies radical transparency, sharing the exact origin and reason for surplus
of every product in each box. This transparency model builds consumer trust and
creates a differentiated narrative around "ugly" or oversupplied produce.
Rescued partners with farmers to create a reliable commercial channel for food
that would otherwise be ploughed back into fields or sent to anaerobic
digestion, providing farmers with additional revenue and consumers with
reduced-price food. The subscription model creates predictable demand that
helps farmers plan surplus diversion in advance, rather than reacting to
rejection after harvest.

#### Classification

**topic_tags:** Food & Agriculture, Business
**circular_model_primary:** Resource Recovery
**circular_sub_models:** Waste-as-resource (industrial symbiosis), Take-back / gamified returns, Recycle / upcycle
**loop_type_emf:** Biological cycle
**value_chain_stage:** Distribution, Product Use, End of Life, Cross-stage
**material_resource_loop:** Surplus and cosmetically imperfect food from farms (fruits, vegetables, and other produce that would otherwise go to waste) -- biological waste-to-consumer loop

#### Linear Model Replaced

Cosmetically imperfect or surplus farm produce rejected by retailers and either
ploughed back into fields, sent to anaerobic digestion, or sent to landfill,
with no commercial value recovered and farmers absorbing the loss.

**inefficiency_type:** Wasted end-of-life value, Unexploited customer engagement

#### Business Model

**revenue_model:** Subscription box sales (direct-to-consumer, recurring revenue); farmer supply partnerships
**pricing_mechanism:** Subscription pricing (regular delivery cadence at a discount to conventional retail)
**technology_enabler:** Direct-to-consumer e-commerce and subscription management platform; provenance tracking to support radical transparency labeling

#### Users and Partners

**target_users:** Primary: UK consumers seeking reduced-price, sustainably sourced food with a transparent provenance story. Secondary: Farmers and producers with surplus or cosmetically rejected produce seeking a commercial diversion channel.
**value_propositions:** Consumers: affordable food with a verified food-waste-reduction story and full provenance transparency. Farmers: reliable commercial revenue from produce that would otherwise be wasted.
**partnerships:** UK farmers and agricultural producers (surplus supply); logistics and cold-chain partners for subscription box delivery

#### Impact and Context

**quantified_impact:** Creates a commercial market for produce that would otherwise be ploughed back into fields or sent to anaerobic digestion; provides farmers with additional revenue on waste streams; reduces consumer food spend relative to conventional retail.
**regulatory_policy_enabler:** UK food waste reduction commitments; Courtauld Commitment; WRAP food waste targets; growing retailer sustainability reporting requirements that create pressure on supply chains to demonstrate waste diversion.
**barriers_challenges:** Maintaining consistent supply of quality surplus produce across seasons; logistics and cold-chain cost for subscription delivery; consumer retention in the subscription model; educating consumers on cosmetic imperfection as no indicator of edibility.
**replication_model:** Direct replication possible for any direct-to-consumer food startup with access to a farm surplus supply network; subscription model and transparency layer are the core differentiators.

#### Prototype Readiness

**circular_maturity_prior:** Low (most farm surplus goes to waste streams or low-value feed; direct-to-consumer surplus channels are nascent)
**capability_requirements:** Reliable farm surplus supply network with forward supply planning capability; subscription e-commerce and logistics infrastructure; provenance tracking and storytelling capability; consumer acquisition and retention for subscription model.
**economic_regulatory_pressure:** Consumer demand shift; regulatory / compliance pressure (food waste targets); internal mandate or leadership commitment
**success_criteria:** New revenue or market access; brand differentiation; emissions or resource reduction target
**prototype_readiness_statement:** A farmer or agricultural cooperative with predictable surplus or cosmetically rejected produce partners with a direct-to-consumer platform that curates weekly or bi-weekly subscription boxes; each box carries item-level provenance disclosure explaining why each product was surplus; consumers pay a discounted subscription price and receive a transparent impact summary per delivery, while the farmer receives a reliable commercial revenue stream on produce that would otherwise be wasted.

---

### FWU-003

**id:** FWU-003
**title:** Alternative Meat Made from Food By-Products
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/planetarians
**confidence_score:** High

#### Organization

**org_name:** Planetarians
**org_one_liner:** Planetarians uses Solid State Fermentation with fungi to convert waste carbohydrates from the vegetable oil, brewing, and distilling industries into high-protein alternative meat ingredients, turning industrial food by-products into a commercial protein source without the need for animals.
**org_profile:** Size: Startup | Industry: Food Technology / Alternative Protein | Type: B2B
**founding_maturity:** Early stage | Maturity: Pilot / Early Growth
**geography:** United States (headquarters); global food industry supply chain relevance

#### Description

Planetarians uses Solid State Fermentation (SSF) with fungi to convert waste
carbohydrates from the vegetable oil, brewing, and distilling industries into
high-protein alternative meat ingredients. The company frames its value
proposition as "processing animal feed into meat, without the need for animals."
The fermentation process is cost-effective, leverages existing food
infrastructure, and provides a circular solution to both food waste valorisation
and global protein demand simultaneously. By transforming industrial food
by-products into a commercially viable protein ingredient, Planetarians
eliminates both the waste disposal problem for its input partners and the virgin
agricultural land, water, and emissions cost of conventional alternative protein
production.

#### Classification

**topic_tags:** Food & Agriculture, Business
**circular_model_primary:** Resource Recovery
**circular_sub_models:** Waste-as-resource (industrial symbiosis), Circular supplies, Recycle / upcycle
**loop_type_emf:** Biological cycle
**value_chain_stage:** Production, End of Life, Cross-stage
**material_resource_loop:** Waste carbohydrates from vegetable oil, brewing, and distilling industries converted via fungal Solid State Fermentation into alternative meat protein ingredients -- industrial by-product to food ingredient loop

#### Linear Model Replaced

Industrial carbohydrate waste from food processing sent to low-value animal
feed or waste streams, while the alternative protein industry simultaneously
uses virgin agricultural inputs (soy, pea, wheat) to manufacture protein
ingredients at high land, water, and energy cost.

**inefficiency_type:** Wasted end-of-life value, Unsustainable materials

#### Business Model

**revenue_model:** B2B ingredient sales to food manufacturers and alternative protein brands; potential co-valorisation revenue from waste input partners (gate fee or cost-share model)
**pricing_mechanism:** Ingredient wholesale pricing; cost savings vs. conventional alternative protein inputs as the primary value lever for buyers
**technology_enabler:** Solid State Fermentation (SSF) platform using fungi; existing food processing infrastructure adaptable for SSF at scale; fermentation process IP

#### Users and Partners

**target_users:** Primary: Food manufacturers and alternative meat brands seeking lower-cost, lower-footprint protein ingredients. Secondary: Vegetable oil processors, breweries, and distilleries generating carbohydrate waste streams seeking disposal or valorisation solutions.
**value_propositions:** Food manufacturers: cost-competitive, high-protein ingredient with a credible circular supply chain story. Waste generators: commercial valorisation of by-product streams that currently cost money to dispose of.
**partnerships:** Vegetable oil processors, breweries, and distilleries (waste input suppliers); food manufacturers and alternative protein brands (ingredient buyers); food technology accelerators and impact investors

#### Impact and Context

**quantified_impact:** Converts industrial food processing waste carbohydrates into commercial protein ingredients, displacing virgin agricultural inputs in alternative protein production; exact volume and emissions figures not stated in source.
**regulatory_policy_enabler:** Growing regulatory and market pressure on alternative protein industry to reduce land and water footprint; food waste valorisation incentives in US and EU food policy; novel food ingredient approval pathways in key markets.
**barriers_challenges:** Regulatory approval for novel fermented food ingredients in target markets; scaling SSF production capacity; consumer and manufacturer acceptance of fungal fermentation-derived protein; securing reliable and consistent waste carbohydrate supply from industrial partners.
**replication_model:** Technology licensing or joint venture with food processors in adjacent geographies; SSF platform adaptable to other waste carbohydrate streams beyond current inputs.

#### Prototype Readiness

**circular_maturity_prior:** Low (industrial food waste streams typically have no protein recovery pathway; alternative protein inputs are predominantly virgin agricultural)
**capability_requirements:** Solid State Fermentation technology and process IP; food safety and novel ingredient regulatory capability; B2B commercial partnerships with both waste generators and food manufacturers; fermentation scale-up infrastructure.
**economic_regulatory_pressure:** Resource cost or scarcity; consumer demand shift; regulatory / compliance pressure (novel food and waste valorisation)
**success_criteria:** Cost reduction; new revenue or market access; emissions or resource reduction target; supply chain resilience
**prototype_readiness_statement:** An industrial food processor generating carbohydrate-rich by-products (spent grain from a brewery, defatted meal from a vegetable oil plant) enters a valorisation partnership with a fermentation technology company; the by-product stream is processed via Solid State Fermentation into a high-protein ingredient sold to alternative protein manufacturers; the food processor receives a valorisation payment or gate-fee credit instead of paying for waste disposal, while the ingredient buyer sources a lower-cost, lower-footprint protein input with a documented circular provenance.

---

### FWU-004

**id:** FWU-004
**title:** Using Every Part of the Climate-Friendly Sorghum Crop
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/using-every-part-of-the-climate-friendly-sorghum-crop-gabanna-foodworks-and
**confidence_score:** High

#### Organization

**org_name:** Gabanna Foodworks; VORM; Springtail; Howard Koster (farmer); Rechstreex
**org_one_liner:** Gabanna Foodworks leads a five-partner Dutch consortium that uses the entire sorghum plant -- grain, stalks, and leaves -- across food and non-food applications, eliminating crop waste while building commercial business models around a regenerative, climate-resilient crop.
**org_profile:** Size: SME / Consortium | Industry: Food & Agriculture / Regenerative Food Systems | Type: B2B2C
**founding_maturity:** Big Food Redesign Challenge participant | Maturity: Pilot
**geography:** Netherlands

#### Description

Gabanna Foodworks, a Dutch food company and Big Food Redesign Challenge
participant, leads a five-partner collaboration that uses the entire sorghum
plant -- grain, stalks, and leaves -- across food and non-food applications to
eliminate crop waste. The consortium includes real estate developer VORM,
specialist wholesaler Springtail, farmer Howard Koster, and local retailer
Rechstreex. Sorghum is a climate-resilient, drought-tolerant grain that
improves soil structure, and the project develops business models that enable
multiple parts of the crop to generate commercial value simultaneously, creating
a full-loop use model for a regenerative crop. The collaboration is notable for
its cross-sector partnership structure, combining food, real estate, retail, and
agriculture into a single whole-plant circular model.

#### Classification

**topic_tags:** Food & Agriculture, Biodiversity, Business
**circular_model_primary:** Circular Inputs
**circular_sub_models:** Circular supplies, Sustainable product design, Waste-as-resource (industrial symbiosis)
**loop_type_emf:** Biological cycle
**value_chain_stage:** Design, Production, End of Life, Cross-stage
**material_resource_loop:** Sorghum crop (whole-plant use -- grain for food, stalks and leaves for non-food applications); regenerative soil-improving crop replacing resource-intensive conventional grain alternatives

#### Linear Model Replaced

Conventional grain agriculture where only the grain fraction is commercialized
and crop residues (stalks, leaves) are treated as agricultural waste, while
farming relies on resource-intensive, non-regenerative crops with high water
and input demand.

**inefficiency_type:** Wasted end-of-life value, Unsustainable materials

#### Business Model

**revenue_model:** Multi-stream revenue across food products (grain), biomaterials or construction inputs (stalks, leaves), and potentially carbon or biodiversity credits from regenerative land management; consortium cost and revenue sharing model
**pricing_mechanism:** Wholesale and retail product sales across food and non-food verticals; grant and challenge-prize funding at pilot stage
**technology_enabler:** Whole-plant crop processing capability for food and non-food fractions; consortium coordination and contract farming arrangements; sorghum agronomy expertise

#### Users and Partners

**target_users:** Primary: Food manufacturers and consumers seeking climate-resilient grain ingredients. Secondary: Construction or materials industries seeking bio-based crop residue inputs; farmers seeking commercially viable regenerative crop alternatives.
**value_propositions:** Farmers: full-crop commercial value (not just grain) from a lower-input, soil-improving crop. Food manufacturers and retailers: a verified regenerative ingredient with biodiversity and climate credentials. Non-food partners: a bio-based, locally sourced material input from agricultural by-products.
**partnerships:** Gabanna Foodworks (food lead); VORM (real estate / non-food application); Springtail (wholesale distribution); Howard Koster (farm / primary production); Rechstreex (retail / local market)

#### Impact and Context

**quantified_impact:** Eliminates crop residue waste from sorghum cultivation by commercializing grain, stalks, and leaves simultaneously; sorghum's drought tolerance and soil-improving properties reduce input requirements vs. conventional grains; exact volume figures not stated in source.
**regulatory_policy_enabler:** EU Common Agricultural Policy reform toward regenerative and biodiversity-supporting farming practices; Dutch national nitrogen reduction targets creating demand for lower-input crop alternatives; EU Farm to Fork Strategy sustainability requirements.
**barriers_challenges:** Developing commercially viable markets for non-food crop fractions (stalks, leaves) at scale; coordinating a multi-partner consortium across food and non-food sectors; consumer familiarity with sorghum as a food ingredient; agronomic scaling of sorghum cultivation in the Netherlands.
**replication_model:** Whole-plant crop model replicable for other underutilized or climate-resilient crops (hemp, miscanthus, amaranth) with multi-sector consortium partnerships linking food and non-food applications.

#### Prototype Readiness

**circular_maturity_prior:** Low (crop residue waste is the norm across most grain agriculture; whole-plant commercialization is rare outside established industrial crops)
**capability_requirements:** Agronomy and crop processing expertise across food and non-food fractions; multi-sector consortium governance structure; market development capability for novel food ingredients and bio-based materials; grant and challenge-prize management at pilot stage.
**economic_regulatory_pressure:** Regulatory / compliance pressure (EU CAP reform, nitrogen reduction); consumer demand shift (regenerative food); resource cost or scarcity
**success_criteria:** Emissions or resource reduction target; new revenue or market access; supply chain resilience; brand differentiation
**prototype_readiness_statement:** A farmer cultivating a climate-resilient, whole-plant-use crop (sorghum, hemp, or amaranth) enters a consortium agreement with a food company, a non-food materials buyer, and a local retailer; the grain fraction is developed as a consumer food product, the stalks or leaves are sold as a bio-based material input to the non-food partner, and the farmer receives revenue from all three fractions simultaneously; the retailer co-brands the food product with the full-crop provenance story, and the consortium applies for regenerative agriculture grants to fund agronomic scale-up.

---

### FWU-005

**id:** FWU-005
**title:** Making New Products from Urban Organic Waste Streams
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/de-clique
**confidence_score:** High

#### Organization

**org_name:** De Clique
**org_one_liner:** De Clique uses cycle couriers and electric vehicles to collect urban food by-products -- coffee grounds, orange peels, and other organic waste -- as pure separated streams from Amsterdam businesses, and sells these to innovators and product manufacturers who transform them into cosmetics, food ingredients, and biomaterials.
**org_profile:** Size: SME / Startup | Industry: Urban Waste Logistics / Circular Materials | Type: B2B
**founding_maturity:** Operational in Amsterdam | Maturity: Growth
**geography:** Netherlands (Amsterdam)

#### Description

De Clique uses cycle couriers and electric vehicles to collect food by-products
-- coffee grounds, orange peels, and other organic waste -- as pure separated
streams from Amsterdam businesses, and sells these to third-party innovators
and product manufacturers who transform them into cosmetics, food ingredients,
and biomaterials. The purity of each collected stream is the core value
proposition: by collecting streams separately at source, De Clique preserves
the chemical and material value of each by-product, making it suitable for
high-value upcycling rather than mixed compost or anaerobic digestion.
Currently only 2% of urban organic waste is reused in the Netherlands,
representing an almost entirely untapped material supply base. De Clique's
logistics model -- low-emission urban collection at the point of generation --
addresses the aggregation and purity problem that prevents most urban organic
waste from reaching upcycling markets.

#### Classification

**topic_tags:** Food & Agriculture, Cities, Business
**circular_model_primary:** Resource Recovery
**circular_sub_models:** Waste-as-resource (industrial symbiosis), Recycle / upcycle, Circular supplies
**loop_type_emf:** Biological cycle
**value_chain_stage:** End of Life, Distribution, Cross-stage
**material_resource_loop:** Urban food by-products (coffee grounds, orange peels, organic waste) collected as pure separated streams from businesses and sold to product manufacturers -- biological waste-to-value urban circular loop

#### Linear Model Replaced

Urban organic food by-products collected as mixed waste, sent to anaerobic
digestion or composting with minimal commercial value recovered, while cosmetic,
food ingredient, and biomaterial manufacturers source virgin or imported raw
material inputs.

**inefficiency_type:** Wasted end-of-life value, Unexploited customer engagement

#### Business Model

**revenue_model:** B2B sales of sorted, pure organic waste streams to upcycling manufacturers and innovators; potential service fee or subscription from waste-generating businesses for separated collection
**pricing_mechanism:** Wholesale material sales priced against the avoided disposal cost for businesses and the virgin material cost for buyers; collection service fee to generating businesses
**technology_enabler:** Low-emission urban logistics (cycle couriers, electric vehicles); source-separation collection protocol; material matching platform connecting waste generators with upcycling buyers

#### Users and Partners

**target_users:** Primary: Amsterdam food businesses (cafes, restaurants, juice bars, food processors) generating consistent organic by-product streams. Secondary: Cosmetic manufacturers, food ingredient companies, and biomaterial innovators seeking traceable, high-purity urban organic inputs.
**value_propositions:** Waste generators: a convenient, low-emission collection service that diverts organic by-products from waste streams and may provide a material income or reduced disposal cost. Material buyers: a consistent, traceable, purity-assured supply of urban organic by-products replacing virgin inputs.
**partnerships:** Amsterdam businesses generating food by-products (supply side); cosmetics, food ingredient, and biomaterials manufacturers (demand side); cycle courier and EV logistics partners; Amsterdam city and innovation ecosystem

#### Impact and Context

**quantified_impact:** Only 2% of urban organic waste is currently reused in the Netherlands; De Clique directly targets the 98% untapped gap by creating a logistics and market infrastructure that did not previously exist; exact volume and revenue figures not stated in source.
**regulatory_policy_enabler:** Dutch and EU waste hierarchy legislation prioritising material recovery over energy recovery; Amsterdam Green City ambitions; EU circular economy action plan targets for biological material reuse; Extended Producer Responsibility frameworks creating incentives for waste stream separation at source.
**barriers_challenges:** Ensuring stream purity through behavioral compliance by waste-generating businesses; achieving sufficient urban collection density for logistics unit economics; developing and maintaining a reliable buyer market for each stream type; scaling beyond Amsterdam without city-specific density advantages.
**replication_model:** City-replication model for dense urban food business environments; model most scalable in cities with high cafe / restaurant density, favorable cycling logistics infrastructure, and active circular economy municipal policy.

#### Prototype Readiness

**circular_maturity_prior:** Low (urban organic waste is predominantly mixed and sent to anaerobic digestion; source-separated collection for high-value upcycling is rare outside specialist pilots)
**capability_requirements:** Urban logistics capability (low-emission collection at scale); source-separation training and behavioral compliance infrastructure for waste-generating businesses; material characterization and quality assurance for each stream type; buyer network development across cosmetics, ingredients, and biomaterials sectors.
**economic_regulatory_pressure:** Regulatory / compliance pressure (waste hierarchy, EPR); consumer demand shift (urban sustainability); internal mandate or leadership commitment
**success_criteria:** New revenue or market access; emissions or resource reduction target; cost reduction (for waste generators); supply chain resilience (for material buyers)
**prototype_readiness_statement:** A startup or municipal waste operator in a dense urban area recruits cafes, juice bars, and food businesses to separate coffee grounds, citrus peels, or other consistent organic by-product streams at source; low-emission couriers collect each stream as a pure, labeled batch; the operator sells curated streams to cosmetics formulators, food ingredient developers, or biomaterial researchers who cannot reliably source these inputs otherwise; each waste-generating business receives a disposal cost credit and a verifiable sustainability metric, while the operator earns a margin between the collection fee and the material sale price.

---

## Field Taxonomy and Controlled Vocabularies

This section defines the controlled vocabulary for the key classification fields
used across all entries. Use these definitions to interpret field values during
retrieval and to correctly classify new entries added to this knowledge base.

---

### G -- Circular Business Model (Primary)

The top-level strategic pattern the case exemplifies. Each entry carries exactly
one primary model.

| Value | Definition |
|---|---|
| **Circular Inputs** | Products made from recycled, renewable, or bio-based materials that eliminate the use of virgin or toxic inputs. Includes circular supplies and sustainable product design strategies. |
| **Sharing Platform** | A platform or system that enables users to share, rent, or access products or assets rather than own them outright, increasing utilization rates across the user base. |
| **Product as a Service** | The producer retains ownership of the product and charges customers for the service or performance it delivers (e.g., per use, per outcome, or subscription), creating a financial incentive for durability, efficiency, and end-of-life recovery. |
| **Product Use Extension** | Business models that keep products and components in use for longer through repair, remanufacturing, refurbishment, resale, or upgrading, deferring or avoiding end of life. |
| **Resource Recovery** | Systems that recover energy, materials, or nutrients from products or waste streams at end of life, through recycling, upcycling, anaerobic digestion, composting, or industrial symbiosis. |

---

### H -- Circular Sub-Models

One or more sub-models that describe the specific circular mechanisms deployed
within the primary model. Entries may carry multiple values.

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

The underlying linear economy failure the circular model addresses. Entries may
carry multiple values.

| Value | Definition |
|---|---|
| **Wasted end-of-life value** | Valuable materials, components, or nutrients are lost at end of product or material life, through landfill, incineration, or unrecovered disposal. |
| **Unsustainable materials** | Products or processes rely on virgin, toxic, non-renewable, or ecologically harmful inputs that deplete natural systems. |
| **Premature product life** | Products are discarded or replaced before their functional life is exhausted, due to design, fashion cycles, or lack of repair options. |
| **Underutilised capacity** | Physical assets (products, equipment, space, vehicles) sit idle for a significant portion of their potential productive life. |
| **Unexploited customer engagement** | Existing customer relationships or touchpoints are not used to create circular value, such as no take-back program, no service model, or no loyalty loop. |

---

### AD -- Economic / Regulatory Pressure

The primary external or internal driver that motivated the circular initiative.
Entries may carry multiple values.

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

The primary metric or outcome against which the circular initiative is evaluated.
Entries may carry multiple values.

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

Indicates how fully the case supports a user-facing circular prototype. Used to
assess which entries can be directly adapted for concept generation.

| Value | Definition |
|---|---|
| **Prototype-ready (complete sentence)** | A complete sentence following the pattern: "The user [does X], and in return receives [Y], while the producer closes the [loop name] loop by [doing Z]." All three elements are present and specific enough to prototype a user interaction. All entries in this file meet this standard. |
| **Mechanic present but not prototype-ready** | The circular mechanic is identifiable (e.g., take-back exists, service model exists) but the case lacks sufficient detail on the user interaction, incentive structure, or return exchange to draft a complete prototype sentence. |
| **Design principle only** | The case describes a design philosophy, material choice, or policy framework rather than a discrete product-user interaction. No testable circular exchange between a user and a producer is described. Applies to most policy/governance cases, research projects, and supply-chain-only interventions. |

---

## RAG Usage Notes

### Prompt Matching Guidance

When retrieving entries for prototype generation, prioritize matching on:

1. `circular_model_primary` -- the broadest strategic pattern (Resource Recovery vs. Circular Inputs)
2. `org_profile` -- org size and type (Startup vs. SME vs. consortium; B2B vs. B2C vs. B2B2C)
3. `value_chain_stage` -- where in the chain the target organization operates
4. `inefficiency_type` -- what waste or underperformance the prototype must address
5. `geography` -- for regulatory and cultural context alignment
6. `material_resource_loop` -- the specific food by-product stream or crop fraction involved

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

### Sector-Specific Matching Notes

- **FWU-001 (Toast Ale):** Best analogue for food and beverage companies with
  an identifiable surplus input stream and craft or premium positioning; also
  relevant for any organization exploring open-source circular model sharing.
- **FWU-002 (Rescued):** Best analogue for direct-to-consumer food startups,
  farm cooperatives, or retailers seeking a subscription-based surplus diversion
  channel with a consumer transparency narrative.
- **FWU-003 (Planetarians):** Best analogue for B2B food technology startups
  targeting industrial food processors as waste input partners and alternative
  protein manufacturers as buyers; relevant for any fermentation-based upcycling
  model.
- **FWU-004 (Gabanna / VORM):** Best analogue for multi-partner consortia
  targeting whole-crop or whole-plant commercial value across food and non-food
  verticals; relevant for regenerative agriculture business model design.
- **FWU-005 (De Clique):** Best analogue for urban circular economy startups
  targeting dense business districts; relevant for any model built on pure
  stream separation logistics as the core value creation mechanism.

### Confidence and Data Quality

All entries in this file carry a `confidence_score` of **High**, sourced
directly from the Ellen MacArthur Foundation circular examples database.
Field values marked "Not stated" in the source have been omitted rather than
interpolated. Do not treat omitted fields as negative evidence -- they reflect
source limitations, not model failure.

---

*End of file -- food-waste-upcycling-RAG.md | schema v1.1*
