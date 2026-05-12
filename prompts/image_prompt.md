### Circular Image Generation Prompt

**Aspect Ratio:** 16:9

**Brand Tokens:**
- Headline font: Literata (serif) — use for the title bar and loop name badge
- Label/body font: Nunito Sans — use for all callout labels and narrative text
- Arrow color 1: #4a7c59 (forest green)
- Arrow color 2: #705c30 (warm amber)
- Background: #faf6f0 (warm off-white, slightly textured paper)
- Reward box fill: #faf6f0 with a #705c30 accent border

**Style:**
Generate a professional diagram in a clean **marker sketch / editorial illustration style**. Render on the background color above with bold, confident strokes.

---

**Composition: Two-Panel Layout**

The image is divided into two panels side by side beneath a full-width title bar.

**Title Bar (full width, top):**
Display the title in large bold Literata serif type: "**[LOOP_NAME_CAPS]**"

---

**Left Panel — User Interaction Scene:**

Show a single person physically interacting with the product or system described in `[NARRATIVE_1_TEXT]`. This is a scene illustration, not a diagram — draw the person and the key physical objects involved in the interaction with confident marker strokes.

- Add **labeled callout annotations** (thin lines with Nunito Sans text labels) pointing to the key elements in the scene: the product, the container or interface, and any digital touchpoint (e.g., phone screen, display, scanner).
- In the center between the two panels, place a highlighted reward box containing:
  - A relevant icon (dollar sign, phone, checkmark — whichever fits the reward type)
  - The text: "**[NARRATIVE_2_TEXT]**"
  - Sub-label: "**User Reward**"
- At the bottom of the left panel, place the label: "**User Action**"

---

**Right Panel — Producer Circular Loop:**

Draw a large circular flow diagram. Color the clockwise arrows alternating between forest green #4a7c59 and warm amber #705c30.

- **Center of the circle:** Place a bold circular badge containing the loop name: "**[LOOP_NAME_CAPS]**"
- **Around the circle (4 stage labels):** Derive four logical stage labels from `[NARRATIVE_3_TEXT]` and `[NARRATIVE_4_TEXT]` that describe what the producer does to close the loop. Place them at the top, right, bottom, and left positions outside the circle arrows. Use Nunito Sans for these labels.
- At the bottom of the right panel, place the label: "**Producer Loop**"

---

**Visual Formatting:**
- Use Literata for the title bar and loop name badge; Nunito Sans for all other text.
- Keep all text labels short (3–6 words); break longer phrases across two lines rather than truncating.

### Integration Mapping for your App

When your application triggers this prompt, map your prototype sentence as follows:

| Variable | Prototype Element | Location |
| :--- | :--- | :--- |
| **[LOOP_NAME_CAPS]** | The "Loop Name" | Title bar + loop badge center |
| **[NARRATIVE_1_TEXT]** | User Action | Left panel scene subject |
| **[NARRATIVE_2_TEXT]** | User Receives | Middle reward box |
| **[NARRATIVE_3_TEXT]** | The "Loop Action" | Right panel circle stages (derived) |
| **[NARRATIVE_4_TEXT]** | Producer Closes Loop | Right panel circle stages (derived) |