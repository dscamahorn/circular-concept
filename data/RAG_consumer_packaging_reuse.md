---
rag_id: consumer-packaging-reuse
rag_version: "1.0"
schema_version: "1.2"
# rag_version: increment when entries are added, removed, or corrected
# schema_version: increment when field names, structure, or controlled vocabulary change
created: 2026-04-12
source_file: consumer-packaging-reuse.csv
source_domain: Ellen MacArthur Foundation Circular Economy Examples
topic_domain: Consumer Packaging Reuse
related_files:
  - path: circular_prototype_rag_registry.md
    role: clarifier
    description: Additional context and guidance for interpreting RAG entries
use_case: Retrieval-Augmented Generation knowledge base for generating circular economy concept prototypes. Use these entries to match organization profiles against proven consumer packaging reuse models, extract analogous strategies, and scaffold new circular business model concepts for similar sectors, geographies, and maturity stages.
min_confidence: High
entry_id_prefix: CPR
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
  - founding_date
  - maturity_stage
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
---

# Consumer Packaging Reuse -- Circular Economy RAG Knowledge Base

## Purpose

This file is a structured, retrievable knowledge base of real-world circular
economy case studies focused on consumer packaging reuse. Each entry captures
a verified example drawn from the Ellen MacArthur Foundation circular examples
library. Entries are formatted for RAG (Retrieval-Augmented Generation) use:
each record is self-contained, richly tagged, and includes a prototype
readiness statement suitable for direct use in concept generation prompts.

## How to Use This File

> For general retrieval and prototyping guidance, see [circular_prototype_rag_registry.md](circular_prototype_rag_registry.md), Section 12.

---

## Entries

---

### CPR-001

**id:** CPR-001
**title:** A Nationwide, Shared System for Reusable Packaging
**url:** https://www.ellenmacarthurfoundation.org/a-nationwide-shared-system-for-reusable-packaging
**confidence_score:** High
**retrieval_tags:** circular-inputs, sustainable-product-design, take-back, gamified-returns, recycle-upcycle, technical-cycle, B2B2C, large-enterprise, nonprofit-governance, France, EU, plastics, retail, FMCG, design, product-use, end-of-life, cross-stage, wasted-end-of-life-value, unsustainable-materials, EPR, regulatory-compliance, consumer-demand-shift, emissions-reduction, deposit-return, reusable-packaging, shared-infrastructure, reverse-vending-machines, standardized-container, AGEC-law

#### Organization

**org_name:** Citeo
**org_one_liner:** Citeo is a French nonprofit producer responsibility organization that manages packaging waste recovery and recycling systems on behalf of brands and retailers operating in France.
**org_profile:** Size: Large enterprise | Industry: Packaging / Retail | Type: B2B2C
**founding_date:** June 2025
**maturity_stage:** Pilot
**geography:** France

#### Description

Citeo's ReUse project establishes a large-scale shared infrastructure for reusable packaging across four French regions covering over 16 million people. Shoppers purchase selected products in standardized returnable containers (R-Coeur), then return them in-store via reverse vending machines in exchange for a deposit refund. Retailers, brands, and reuse operators share collection, washing, and logistics infrastructure, reducing per-unit costs. The first phase launched June 2025 with more than 140 product lines, with a national rollout planned for 2027.

#### Classification

**topic_tags:** Plastics, Retail, Business
**circular_model_primary:** Circular Inputs
**circular_sub_models:** Sustainable product design, Take-back / gamified returns, Recycle / upcycle
**loop_type_emf:** Technical cycle
**value_chain_stage:** Design, Product Use, End of Life, Cross-stage
**material_resource_loop:** Standardized reusable consumer packaging (glass and plastic containers)

#### Linear Model Replaced

Single-use consumer packaging sold once and disposed of after use, with materials going to waste or low-grade recycling.

**inefficiency_type:** Wasted end-of-life value, Unsustainable materials

#### Business Model

**revenue_model:** Extended Producer Responsibility (EPR) fees redistributed to fund reuse infrastructure; deposit system revenues (unreturned deposits reinvested)
**pricing_mechanism:** Transaction fee (deposit-return)
**technology_enabler:** Reverse vending machines (RVMs); digital tracking of container flows

#### Users and Partners

**target_users:** Primary: French grocery shoppers in Brittany, Normandy, Pays de la Loire, and Hauts-de-France. Secondary: major retailers (Carrefour, Leclerc, Intermarche, Cooperative U, Monoprix) and 50+ brands
**value_propositions:** Reduced packaging waste and landfill costs; meets regulatory targets; access to shared logistics that no single brand could afford alone
**partnerships:** Cooperative U, Carrefour, Intermarche, Leclerc, Monoprix (retailers -- provide store locations and in-store return machines); 50+ product brands (supply packaged goods); reuse operators (manage collection, washing, and logistics infrastructure)

#### Impact and Replication

**quantified_impact:** First phase: over 140 products in reusable packaging on shelves by June 2025; over 360 stores participating by end of 2025; millions of standardized containers targeted by end of 2026
**replication_model:** Yes -- open-source R-Coeur packaging specifications; national rollout planned for all of France by 2027

#### Context and Pressures

**regulatory_policy_enabler:** France's AGEC Law (Anti-Waste and Circular Economy Law) -- mandates 10% reusable packaging by 2027 and requires a share of EPR fees to fund reuse infrastructure
**economic_regulatory_pressure:** Regulatory / compliance pressure (AGEC Law mandates 10% reusable packaging by 2027 and EPR fees must fund reuse); Consumer demand shift (consumer preference for reduced waste cited)
**success_criteria:** Regulatory compliance (meet 10% reusable packaging target by 2027); Emissions or resource reduction target (significantly reduce waste and preserve valuable materials)

#### Barriers and Capabilities

**barriers_challenges:** Scaling consumer return behavior; ensuring high return rates to make economics viable; complexity of coordinating shared logistics across competing retailers
**circular_maturity_prior:** Not stated
**capability_requirements:** Shared and standardized packaging specification (R-Coeur, open-source); shared logistics, washing, and collection infrastructure across retailers; reverse vending machine network; consumer awareness campaign infrastructure

#### Prototype Readiness Statement

The user purchases a product in a standardized reusable container and returns the empty container to an in-store reverse vending machine, and in return receives a deposit refund, while the producer closes the Deposit-return loop by routing the collected containers through shared washing and refilling infrastructure for reuse by partner brands.

---

### CPR-002

**id:** CPR-002
**title:** PALPA: The Collaboration That Led to Finland's Successful Deposit Return System
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/palpa-the-collaboration-that-led-to-finlands-successful-deposit-return
**confidence_score:** High
**retrieval_tags:** resource-recovery, recycle-upcycle, take-back, gamified-returns, return, technical-cycle, B2B2C, nonprofit, Finland, EU, plastics, beverage, retail, end-of-life, cross-stage, wasted-end-of-life-value, unsustainable-materials, regulatory-compliance, resource-cost-scarcity, cost-reduction, emissions-reduction, deposit-return, beverage-packaging, aluminium, PET, glass, DRS, packaging-tax, reverse-vending-machines

#### Organization

**org_name:** Suomen Palautuspakkaus Oy (PALPA); Alko Oy; Inex Partners Oy; Kesko Oyj; Hartwall Ab; Olvi Oyj; Sinebrychoff Supply Company Oy; Ekopulloyhdistys ry (Ekopullo)
**org_one_liner:** PALPA (Suomen Palautuspakkaus Oy) is a Finnish nonprofit that operates the national deposit-return system for beverage packaging, coordinating collection, logistics, and recycling across retailers, producers, and importers throughout Finland.
**org_profile:** Size: Not stated (nonprofit, ~15 employees) | Industry: Beverage / Packaging / Waste management | Type: B2B2C
**founding_date:** 1996
**maturity_stage:** Operating at scale
**geography:** Finland

#### Description

PALPA is a Finnish nonprofit formed in 1996 by competing retailers and breweries to operate a nationwide deposit-return system (DRS) for beverage packaging. When consumers purchase a beverage, a deposit of EUR 0.10--0.40 is added to the price; after consuming the drink, they return the empty can, glass bottle, or PET bottle to reverse vending machines in grocery stores and receive the deposit back. PALPA coordinates the collection, sorting, transport, and recycling of these containers, with revenue from selling high-quality recycled material and unclaimed deposits reinvested into the system.

#### Classification

**topic_tags:** Plastics, Business, Retail
**circular_model_primary:** Resource Recovery
**circular_sub_models:** Recycle / upcycle, Take-back / gamified returns, Return
**loop_type_emf:** Technical cycle
**value_chain_stage:** End of Life, Cross-stage
**material_resource_loop:** Aluminium beverage cans, PET plastic bottles, glass bottles

#### Linear Model Replaced

Beverage packaging disposed of as general waste after single use, with low recycling rates and high packaging tax liability for producers.

**inefficiency_type:** Wasted end-of-life value, Unsustainable materials

#### Business Model

**revenue_model:** Membership and recycling fees paid by producers and importers; revenue from selling high-quality recycled materials (aluminium, PET, glass); small portion from unreturned deposit float reinvested into system operations
**pricing_mechanism:** Transaction fee (deposit per container circulates through the system)
**technology_enabler:** Reverse vending machines (RVMs) for in-store automated container return and sorting; centralized data system for deposit reimbursement and tax reporting

#### Users and Partners

**target_users:** Primary: Finnish consumers returning beverage containers. Secondary: beverage producers, importers, retailers, hotels, and restaurants -- all entities selling deposit-marked beverages must participate
**value_propositions:** Avoid or significantly reduce Finnish packaging tax liability; access to shared logistics and recycling infrastructure no single company could build alone; recycled material sold back as high-quality feedstock
**partnerships:** Reverse vending machine suppliers (provide in-store RVM hardware); transport contractors (contracted by PALPA for pickup); processing facility operators (sort and bulk materials); recyclers and beverage packaging manufacturers (receive processed materials); Alko Oy (government-owned alcohol retailer, founding member and key return-point network); Ekopullo (operates complementary refillable packaging DRS)

#### Impact and Replication

**quantified_impact:** Over 92% PET bottle recovery rate; 99% aluminium can recovery rate; 99% glass bottle recovery rate; ~EUR 80 million annual turnover; ~EUR 360 million in deposit fees circulating annually
**replication_model:** Yes -- PALPA is actively referenced as a model for other countries designing DRS systems, particularly as EU mandates approach

#### Context and Pressures

**regulatory_policy_enabler:** Finnish packaging tax legislation (1983) -- levied on beverage packaging not part of a DRS; EU membership in 1995 (ended Alko Oy's regulatory monopoly, prompting private-sector collaboration); EU Single-Use Plastics Directive (mandates 90% plastic bottle collection by 2029)
**economic_regulatory_pressure:** Regulatory / compliance pressure (Finnish packaging tax incentivized DRS participation to avoid tax; EU Single-Use Plastics Directive adds urgency); Resource cost or scarcity (producers motivated to avoid packaging tax costs)
**success_criteria:** Cost reduction (avoid or minimize Finnish packaging tax); Regulatory compliance (meet Finnish packaging legislation requirements and EU mandates); Emissions or resource reduction target (recover materials at highest possible quality for reincorporation into new packaging)

#### Barriers and Capabilities

**barriers_challenges:** Initial challenge of getting competing retailers and breweries to share sensitive production data and collaborate; antitrust considerations; ongoing need to expand the system to juice producers and other non-tax-liable sectors
**circular_maturity_prior:** The original DRS was run by state-owned Alko Oy before PALPA's formation. When Finland joined the EU in 1995, Alko Oy's regulatory role ended, directly prompting the formation of PALPA as a private-sector collaborative. Ekopullo, a related nonprofit, was established alongside PALPA to handle refillable packaging separately. PALPA has been operating at national scale since the late 1990s.
**capability_requirements:** Reverse vending machine network across all retail formats; centralized logistics and transport contracting; data aggregation system to share production volumes and deposit flows without exposing competitor data; processing and sorting infrastructure; regulatory reporting capability for Finnish tax authorities

#### Prototype Readiness Statement

The user returns an empty beverage can, PET bottle, or glass bottle to a reverse vending machine in any authorized grocery store or service station, and in return receives a full deposit refund (EUR 0.10--0.40), while the producer closes the Deposit-return loop by routing collected containers through PALPA's centralized sorting, transport, and recycling infrastructure to be reprocessed as high-quality feedstock for new beverage packaging.

---

### CPR-003

**id:** CPR-003
**title:** A Reusable Drinks Bottle Design for Multiple Brands: Universal Bottle
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/a-reusable-drinks-bottle-design-for-multiple-brands-universal-bottle
**confidence_score:** High
**retrieval_tags:** circular-inputs, sustainable-product-design, take-back, gamified-returns, recycle-upcycle, technical-cycle, B2C, large-enterprise, Latin-America, plastics, retail, FMCG, food-and-beverage, design, product-use, end-of-life, wasted-end-of-life-value, unsustainable-materials, regulatory-compliance, consumer-demand-shift, resource-cost-scarcity, emissions-reduction, new-revenue, deposit-return, reusable-packaging, multi-brand, PET, refillable-bottle, standardized-design

#### Organization

**org_name:** Coca-Cola Company; Coca-Cola Bottling Partners
**org_one_liner:** The Coca-Cola Company is one of the world's largest beverage companies, producing and distributing soft drinks in over 200 countries through a global network of bottling partners.
**org_profile:** Size: Large enterprise (Coca-Cola -- one of the world's largest FMCG companies) | Industry: Food and beverage / FMCG | Type: B2C
**founding_date:** 2018
**maturity_stage:** Growth
**geography:** Latin America (primary); scaling to other continents

#### Description

Coca-Cola's Universal Bottle is a standardized reusable PET plastic bottle designed to be filled with multiple soda brands across Latin America. When a consumer finishes a drink, they return the bottle to the point of sale, where producers collect, clean, and refill it -- with each bottle reused up to 25 times before recycling, reducing overall plastic use by 90% per serving compared to single-use bottles. Introduced in 2018, it is Coca-Cola's fastest growing packaging format in Latin America and is being scaled to other continents.

#### Classification

**topic_tags:** Plastics, Retail, Business
**circular_model_primary:** Circular Inputs
**circular_sub_models:** Sustainable product design, Take-back / gamified returns, Recycle / upcycle
**loop_type_emf:** Technical cycle
**value_chain_stage:** Design, Product Use, End of Life
**material_resource_loop:** PET plastic bottles standardized across multiple brands and reused up to 25 times before recycling; 90% reduction in plastic use per serving vs. single-use

#### Linear Model Replaced

Single-use PET soda bottles purchased once, consumed, and disposed of -- generating large volumes of plastic waste per unit of beverage sold.

**inefficiency_type:** Wasted end-of-life value, Unsustainable materials

#### Business Model

**revenue_model:** Beverage product sale; reusable bottle deposit system reduces packaging cost over multiple uses
**pricing_mechanism:** Flat rate (product sale); Deposit-return (consumer deposit on reusable bottle returned at point of sale)
**technology_enabler:** Standardized multi-brand bottle design; in-store collection and return logistics; industrial washing and quality inspection; bottle tracking system

#### Users and Partners

**target_users:** Primary: Latin American soda consumers who purchase and return bottles at local retail points. Secondary: Coca-Cola bottling partners operating the refill and return logistics
**value_propositions:** 90% reduction in plastic use per serving vs. single-use; cost saving through bottle reuse vs. single-use packaging procurement; consumer familiarity with return systems in Latin American markets; Coca-Cola sustainability credentials
**partnerships:** Coca-Cola bottling partners across Latin America (return, washing, and refill operations); retail points of sale (collection hubs); Latin American governments (alignment with plastic reduction regulations)

#### Impact and Replication

**quantified_impact:** Each bottle reused up to 25 times; 90% reduction in plastic use per serving vs. single-use; fastest growing packaging format for Coca-Cola in Latin America since 2018
**replication_model:** Yes -- actively scaling from Latin America to other continents

#### Context and Pressures

**regulatory_policy_enabler:** Latin American plastic packaging regulations; EU Single-Use Plastics Directive (driving global Coca-Cola packaging strategy); deposit-return system legislation in relevant markets
**economic_regulatory_pressure:** Regulatory / compliance pressure (Latin American plastic regulations; EU Single-Use Plastics Directive shaping global Coca-Cola strategy); Consumer demand shift (growing consumer and retailer demand for sustainable beverage packaging in Latin American markets); Resource cost or scarcity (rising virgin PET costs and packaging waste disposal costs making reuse economically attractive at scale)
**success_criteria:** Emissions or resource reduction target (90% reduction in plastic use per serving); New revenue or market access (Universal Bottle as fastest growing format -- growing market share through reuse positioning); Regulatory compliance (meet plastic packaging reduction requirements across Latin American markets)

#### Barriers and Capabilities

**barriers_challenges:** Consumer behavior change to return bottles at point of sale; ensuring bottle return rates high enough to make system economics work; washing and logistics infrastructure investment; scaling the standardized bottle design across diverse retail formats in Latin America
**circular_maturity_prior:** Coca-Cola has operated glass bottle refill systems historically, particularly in Latin America. The Universal Bottle represents the application of refillable packaging principles to PET plastic, modernizing a historic return model for contemporary markets.
**capability_requirements:** Standardized multi-brand bottle mold design and manufacturing; industrial washing and inspection infrastructure at bottling plants; point-of-sale collection logistics; bottle deposit management; consumer communication on return process

#### Prototype Readiness Statement

The user purchases a soda in a Universal Bottle and returns the empty bottle to the point of sale, and in return receives their deposit back, while the producer closes the Deposit-return loop by collecting, washing, inspecting, and refilling the bottle up to 25 times across multiple brands before recycling it -- achieving 90% reduction in plastic use per serving vs. single-use alternatives.

---

### CPR-004

**id:** CPR-004
**title:** An Industry-Wide Shared Packaging System: Swedish Return System
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/an-industry-wide-shared-packaging-system-swedish-return-system
**confidence_score:** High
**retrieval_tags:** sharing-platform, share, circular-supplies, technical-cycle, B2B, large-enterprise, trade-association, Sweden, EU, food-and-agriculture, retail, logistics, product-use, wasted-end-of-life-value, unsustainable-materials, regulatory-compliance, resource-cost-scarcity, internal-mandate, cost-reduction, emissions-reduction, supply-chain-resilience, shared-infrastructure, reusable-crates, food-supply-chain, pooling, fresh-produce, crate-tracking

#### Organization

**org_name:** Swedish Return System (SRS); Trade Association for Grocery of Sweden; Swedish Food and Drinks Retailers Association
**org_one_liner:** The Swedish Return System (SRS) is a B2B shared pool of reusable plastic crates and pallets established in 1997 and jointly owned by two Swedish grocery trade associations, used to deliver fresh produce across 1,500+ participating businesses.
**org_profile:** Size: Large enterprise (trade association-owned, 1,500+ members) | Industry: Food and agriculture / Logistics / Packaging | Type: B2B
**founding_date:** 1997
**maturity_stage:** Operating at scale
**geography:** Sweden

#### Description

The Swedish Return System (SRS) is a B2B shared pool of reusable plastic crates and pallets used to deliver fresh produce across the Swedish food and drinks industry, established in 1997. Over 1,500 businesses participate in the system, which is jointly owned by the two main Swedish grocery trade associations. Businesses pay a user fee and/or daily rent to participate, and reusable crates circulate continuously through the supply chain rather than being disposed of after each use. Over 50% of all fresh produce in Sweden is now delivered in reusable SRS packaging.

#### Classification

**topic_tags:** Food and agriculture, Business, Retail
**circular_model_primary:** Sharing Platform
**circular_sub_models:** Share, Circular supplies
**loop_type_emf:** Technical cycle
**value_chain_stage:** Logistics, Product Use
**material_resource_loop:** Reusable plastic crates and pallets circulating continuously through the Swedish food supply chain -- replacing single-use cardboard and wooden crates

#### Linear Model Replaced

Fresh produce delivered in single-use cardboard or wooden crates discarded after each delivery -- generating large volumes of packaging waste and requiring continuous virgin material input.

**inefficiency_type:** Wasted end-of-life value, Unsustainable materials

#### Business Model

**revenue_model:** User fees and/or daily rental charges paid by participating businesses; system jointly owned by two trade associations as a nonprofit pooling model
**pricing_mechanism:** Flat rate (daily rental); Transaction fee (per-use fee)
**technology_enabler:** Crate tracking and inventory management system; washing and quality inspection infrastructure; logistics coordination across 1,500+ businesses

#### Users and Partners

**target_users:** Primary: Swedish food producers, distributors, and retailers participating in the shared crate pool. Secondary: Swedish consumers benefiting from a more efficient and lower-waste food supply chain
**value_propositions:** Elimination of single-use packaging cost for each delivery; reduced waste disposal burden; standardized crates improving handling efficiency; collective infrastructure unavailable to any individual company; over 50% of Swedish fresh produce delivered more sustainably
**partnerships:** Trade Association for Grocery of Sweden (co-owner); Swedish Food and Drinks Retailers Association (co-owner); 1,500+ participating food businesses; crate washing and logistics service providers

#### Impact and Replication

**quantified_impact:** Over 50% of all fresh produce in Sweden delivered in reusable SRS packaging; 1,500+ participating businesses; system founded 1997 and operating continuously for 25+ years
**replication_model:** Yes -- the SRS model has been studied internationally as a model for B2B shared packaging systems in food supply chains

#### Context and Pressures

**regulatory_policy_enabler:** Swedish and EU packaging waste reduction legislation; EU Packaging and Packaging Waste Regulation (driving demand for reusable B2B packaging systems)
**economic_regulatory_pressure:** Regulatory / compliance pressure (Swedish and EU packaging waste legislation; EU Packaging and Packaging Waste Regulation); Resource cost or scarcity (cost of single-use packaging at scale for 1,500+ businesses making shared reusable system economically attractive); Internal mandate or leadership commitment (trade association decision to establish shared infrastructure as a collective benefit)
**success_criteria:** Cost reduction (eliminate single-use crate cost for 1,500+ member businesses); Emissions or resource reduction target (replace single-use cardboard and wooden crates for over 50% of Swedish fresh produce); Supply chain resilience (standardized shared crate pool improving handling efficiency across the supply chain)

#### Barriers and Capabilities

**barriers_challenges:** Managing crate loss and damage across 1,500+ businesses; maintaining washing and quality standards; coordinating return logistics across a complex multi-party supply chain; ensuring all participating businesses return crates promptly
**circular_maturity_prior:** SRS was established in 1997 as a deliberate industry-wide circular infrastructure investment. The system has been operating for 25+ years -- representing a mature, fully scaled circular economy model rather than a pilot.
**capability_requirements:** Shared crate pool management and tracking across 1,500+ businesses; industrial washing and quality inspection facilities; return logistics coordination; trade association governance and membership management; crate replacement and capital investment planning

#### Prototype Readiness Statement

The user (food business) loads fresh produce into SRS reusable crates for delivery, and in return accesses standardized, clean packaging at a daily rental fee without purchasing or disposing of single-use crates, while the producer closes the Sharing platform loop by pooling crates across 1,500+ businesses -- washing, inspecting, and recirculating them continuously rather than disposing of packaging after each delivery.

---

### CPR-005

**id:** CPR-005
**title:** Beyond the Bag: A Collective Effort to Drive Customers Away from Single-Use Bags
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/beyond-the-bag-a-collective-effort-to-drive-customers-away-from-single-use
**confidence_score:** High
**retrieval_tags:** circular-inputs, sustainable-product-design, share, technical-cycle, B2C, large-enterprise, United-States, plastics, retail, product-use, end-of-life, wasted-end-of-life-value, unexploited-customer-engagement, regulatory-compliance, consumer-demand-shift, competitor-market-pressure, emissions-reduction, brand-differentiation, cost-reduction, single-use-bags, BYOB, consumer-behavior, collective-action, bag-fee, open-source-campaign

#### Organization

**org_name:** Consortium to Reinvent the Retail Bag (Closed Loop Partners' Center for the Circular Economy); CVS Health; Target; Walmart; Kroger; Dollar Tree; Meijer
**org_one_liner:** Closed Loop Partners is a US-based investment firm and innovation center that funds and develops circular economy solutions across consumer goods, retail, and waste sectors.
**org_profile:** Size: Large enterprise | Industry: Retail | Type: B2C
**founding_date:** 2020
**maturity_stage:** Growth
**geography:** United States (Denver, Colorado; Tucson, Arizona; Southern California -- expanded 2025)

#### Description

A consortium of major US retailers convened by Closed Loop Partners piloted and then scaled a multi-city campaign to shift shoppers away from single-use plastic bags. After years of testing reuse solutions including borrow-a-bag schemes and incentive programs, the coalition distilled its findings into a unified Bring Your Own Bag campaign deployed across over 375 stores in two cities. The campaign used shared signage, cashier prompts, and community outreach to make reusable bag behavior habitual.

#### Classification

**topic_tags:** Plastics, Retail, Business
**circular_model_primary:** Circular Inputs
**circular_sub_models:** Sustainable product design, Share
**loop_type_emf:** Technical cycle
**value_chain_stage:** Product Use, End of Life
**material_resource_loop:** Single-use plastic shopping bags

#### Linear Model Replaced

Single-use plastic bags dispensed at checkout and discarded after each use, with less than 10% recycled globally.

**inefficiency_type:** Wasted end-of-life value, Unexploited customer engagement

#### Business Model

**revenue_model:** Funded by member retailer contributions; CVS, Target, and Walmart collectively committed over USD 15 million to launch; no direct revenue model -- initiative is cost-avoidance and brand value driven
**pricing_mechanism:** Not applicable -- funded by retailer contributions, not a consumer-facing pricing model
**technology_enabler:** Digital data collection and onsite observation; open-source campaign assets distributed digitally; no primary enabling technology

#### Users and Partners

**target_users:** Primary: everyday grocery and retail shoppers in US cities. Secondary: city governments, nonprofits, and local business groups as co-distributors of the campaign
**value_propositions:** Reduced per-store bag costs; regulatory compliance in fee-mandated cities; shared consumer behavior shift that no single brand could achieve alone
**partnerships:** OpenIDEO (innovation challenge platform); city governments of Denver and Tucson (policy enforcement and community outreach); local nonprofits and business groups (campaign amplification); Closed Loop Partners / Center for the Circular Economy (secretariat and research)

#### Impact and Replication

**quantified_impact:** Nearly 5% reduction in single-use bag use over three months across two cities (2.1 million people reached); 11% reduction in Denver; 2% in Tucson; equivalent to preventing ~9.5 million single-use bags annually
**replication_model:** Yes -- open-source campaign assets (signage, social media, training); scaling to Southern California with ~1,000 stores in 2025--2026

#### Context and Pressures

**regulatory_policy_enabler:** Denver, Colorado: USD 0.10 single-use bag fee (municipal ordinance) -- measurably amplified campaign impact (11% vs. 2% reduction)
**economic_regulatory_pressure:** Regulatory / compliance pressure (municipal bag bans and fee legislation prompted retailer action); Consumer demand shift (consumer sustainability expectations cited); Competitor or market pressure (collective action needed to shift systemic consumer behavior)
**success_criteria:** Emissions or resource reduction target (prevent ~9.5 million single-use bags annually); Brand differentiation (shared credibility and market signal); Cost reduction (lower per-store bag costs)

#### Barriers and Capabilities

**barriers_challenges:** Consumer behavior change is slow without policy backup; ensuring cashier prompt consistency across hundreds of stores; achieving near-term behavior change vs. long-term habit formation
**circular_maturity_prior:** The Consortium spent 2020--2022 in innovation and piloting phase before pivoting to the tactical campaign in 2023. The borrow-a-bag model was tested and found less scalable than simpler behavioral nudges. The Playbook was developed as a distillation of learnings before the campaign launched. Next step is scaling to Southern California (~1,000 stores).
**capability_requirements:** Unified cross-retailer campaign coordination infrastructure; open-source asset library; onsite data collection and observation methodology; cashier training protocols; city-level government and nonprofit partnerships

#### Prototype Readiness Statement

The user brings their own bag or declines a single-use bag at checkout prompted by in-store signage and cashier reminders, and in return saves money (in fee markets) and participates in a visible community norm, while the producer closes the Sharing platform loop by coordinating cross-retailer behavior change infrastructure that reduces single-use bag waste at city scale.

---

### CPR-006

**id:** CPR-006
**title:** Pay for the Product, Not the Packaging: Algramo
**url:** https://www.ellenmacarthurfoundation.org/circular-examples/pay-for-the-product-not-the-packaging-algramo
**confidence_score:** High
**retrieval_tags:** sharing-platform, pay-per-use, take-back, gamified-returns, technical-cycle, B2B2C, SME, Chile, United-States, Indonesia, plastics, retail, FMCG, product-use, end-of-life, unsustainable-materials, wasted-end-of-life-value, unexploited-customer-engagement, regulatory-compliance, consumer-demand-shift, internal-mandate, new-revenue, emissions-reduction, brand-differentiation, refill, smart-dispensing, RFID, household-products, low-income, micro-quantities, plastic-free, mobile-app

#### Organization

**org_name:** Algramo
**org_one_liner:** Algramo is a Chilean company that operates a smart refill system enabling consumers to refill RFID-chipped reusable containers with household cleaning and personal care products at app-connected dispensing machines, eliminating single-use packaging.
**org_profile:** Size: SME | Industry: Retail technology / FMCG / Packaging | Type: B2B2C
**founding_date:** Not stated
**maturity_stage:** Growth
**geography:** Chile (Santiago); United States (New York); Indonesia (Jakarta)

#### Description

Algramo is a Chilean company that operates a smart refill system enabling consumers to refill reusable packaging with household cleaning and personal care products using RFID-chipped containers and app-connected dispensing machines. Customers credit an account via a mobile app and bring their smart container to an Algramo dispenser, which recognizes the container and dispenses the exact quantity desired. Serving brands including Quix, Omo, Pinesol, and Clorox, Algramo eliminates single-use packaging at point of sale while making products accessible in micro-quantities to low-income consumers.

#### Classification

**topic_tags:** Plastics, Retail, Business
**circular_model_primary:** Sharing Platform
**circular_sub_models:** Pay-per-use, Take-back / gamified returns
**loop_type_emf:** Technical cycle
**value_chain_stage:** Product Use, End of Life
**material_resource_loop:** Single-use household product packaging eliminated through reusable RFID-chipped container and smart dispensing refill system

#### Linear Model Replaced

Household cleaning and personal care products sold in single-use plastic packaging purchased repeatedly, generating large plastic waste volumes particularly in emerging market contexts.

**inefficiency_type:** Unsustainable materials, Wasted end-of-life value, Unexploited customer engagement

#### Business Model

**revenue_model:** Transaction commission on each dispensed product refill; hardware leasing or sale of dispensing machines to retail partners; potential brand partnership fees from FMCG companies
**pricing_mechanism:** Pay-per-use (charged per quantity dispensed)
**technology_enabler:** RFID-chipped reusable containers; smart dispensing machines with app connectivity; mobile payment and account credit system

#### Users and Partners

**target_users:** Primary: low-to-middle income consumers in Chile, Indonesia, and the US seeking affordable access to household products in micro-quantities without paying a packaging premium. Secondary: FMCG brands seeking to offer products through a plastic-free channel
**value_propositions:** Pay only for product -- no packaging cost; access products in micro-quantities matching actual purchase power; eliminate single-use plastic from household product consumption; convenience of app-based payment and automatic container recognition
**partnerships:** Quix, Omo, Pinesol, Clorox (FMCG brand partners supplying products for dispensing); retail partners hosting dispensing machines; mobile payment providers; impact investors

#### Impact and Replication

**quantified_impact:** Over 250,000 packaging units put into market in 2020, all 100% reusable
**replication_model:** Yes -- Algramo has expanded from Chile to New York and Jakarta, demonstrating active international replication

#### Context and Pressures

**regulatory_policy_enabler:** Chilean plastic bag and packaging regulations; US and Indonesian plastic pollution policies; growing municipal plastic reduction mandates
**economic_regulatory_pressure:** Regulatory / compliance pressure (plastic packaging regulations in Chile, US, and Indonesia); Consumer demand shift (consumer demand for lower-cost product access without packaging premium, particularly in emerging markets); Internal mandate or leadership commitment (Algramo founded to address the social equity dimension of single-use packaging costs for low-income consumers)
**success_criteria:** New revenue or market access (build a transaction-based revenue model across three international markets); Emissions or resource reduction target (eliminate single-use plastic packaging from household product consumption for participating users); Brand differentiation (establish Algramo as the leading reuse infrastructure platform for FMCG brands globally)

#### Barriers and Capabilities

**barriers_challenges:** Achieving sufficient dispenser network density for consumer convenience; consumer behavior change to bring container to dispenser; RFID container unit economics vs. single-use packaging cost; FMCG brand partner willingness to invest in alternative distribution channel
**circular_maturity_prior:** Algramo began in Chile with dry goods refill and has expanded to liquid household products and three international cities. The RFID-chipped container system represents a significant technology evolution from earlier simpler dispensing models.
**capability_requirements:** RFID-chipped container manufacturing and distribution; smart dispensing machine hardware development and maintenance; mobile app and payment platform; FMCG brand partnership development; retail network partnerships for dispenser placement

#### Prototype Readiness Statement

The user brings their RFID-chipped Algramo container to a smart dispensing machine, selects their product and quantity via the app, and receives the exact quantity dispensed without single-use packaging, while the producer closes the Pay-per-use loop by charging only for the product consumed -- eliminating the packaging cost premium -- and the Deposit-return loop by keeping the smart container in continuous circulation.

---

## Field Taxonomy and Controlled Vocabularies

> Controlled vocabulary for all classification fields (G, H, AC, AD, AE, AH) is maintained in [circular_prototype_rag_registry.md](circular_prototype_rag_registry.md), Section 11. Do not edit definitions here.

---

## RAG Usage Notes

> General retrieval priorities and prototype generation template: see [circular_prototype_rag_registry.md](circular_prototype_rag_registry.md), Section 12.

### Sector-Specific Matching Notes

- **CPR-001 (Citeo):** Best analogue for brands or industry bodies designing multi-party shared packaging infrastructure; most relevant where EPR legislation requires collective reuse investment and no single brand can build the system alone.
- **CPR-002 (PALPA):** Best analogue for national or regional deposit-return system design; most relevant for beverage producers facing packaging tax liability or DRS mandate, and for cooperative governance models across competing industry players.
- **CPR-003 (Coca-Cola Universal Bottle):** Best analogue for a single large FMCG brand launching a proprietary reusable packaging format at scale; most relevant where the brand controls its own bottling or distribution and can drive the return loop directly.
- **CPR-004 (Swedish Return System):** Best analogue for B2B supply chain packaging shared across a trade sector; most relevant for food, agriculture, or logistics organizations exploring pooled asset models governed by a trade association or cooperative.
- **CPR-005 (Beyond the Bag):** Best analogue for retailer consortia or collective consumer behavior-change campaigns; most relevant in markets with bag fee or ban legislation, where shared signage and cashier prompts are sufficient infrastructure.
- **CPR-006 (Algramo):** Best analogue for refill or dispensing models eliminating single-use packaging at point of sale; most relevant for FMCG brands targeting urban, sustainability-conscious, or low-income consumer segments via smart infrastructure rather than store redesign.

---

*End of file -- consumer-packaging-reuse-RAG.md | schema v1.2*
