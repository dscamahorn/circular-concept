### Circular Image Generation Prompt

**Aspect Ratio:** 16:9

**Style & Brand Identity:**
Generate a professional diagram in a clean **marker sketch / editorial illustration style**. The visual language (color palette, line weight, and typography) must strictly follow the specifications outlined in the **DESIGN.md** file. Render the image on a slightly textured, off-white paper background with bold, confident strokes.

---

**Composition: Two-Panel Layout**

The image is divided into two panels side by side beneath a full-width title bar.

**Title Bar (full width, top):**
Display the title in large bold serif type: "**[LOOP_NAME_CAPS]**"

---

**Left Panel — User Interaction Scene:**

Show a single person physically interacting with the product or system described in `[NARRATIVE_1_TEXT]`. This is a scene illustration, not a diagram — draw the person and the key physical objects involved in the interaction with confident marker strokes.

- Add **labeled callout annotations** (thin lines with text labels) pointing to the key elements in the scene: the product, the container or interface, and any digital touchpoint (e.g., phone screen, display, scanner).
- In the center between the two panels, place a highlighted reward box containing:
  - A relevant icon (dollar sign, phone, checkmark — whichever fits the reward type)
  - The text: "**[NARRATIVE_2_TEXT]**"
  - Sub-label: "**User Reward: Y**"
- At the bottom of the left panel, place the label: "**User Action: X**"

---

**Right Panel — Producer Circular Loop:**

Draw a large circular flow diagram. Use two arrow colors from **DESIGN.md** alternating around the circle to show the continuous loop motion (clockwise).

- **Center of the circle:** Place a bold circular badge containing the letter "**Z**" and the loop name from `[LOOP_NAME_CAPS]` in smaller text beneath it.
- **Around the circle (4 stage labels):** Derive four logical stage labels from `[NARRATIVE_3_TEXT]` and `[NARRATIVE_4_TEXT]` that describe what the producer does to close the loop. Place them at the top, right, bottom, and left positions outside the circle arrows.
- At the bottom of the right panel, place the label: "**Producer Loop: Z**"

---

**Visual Formatting:**
- Use the hex codes from **DESIGN.md** to color-code the circular arrows and reward box.
- Use the "Design System" fonts for all labels and headers.
- Do not display variable names (X, Y, Z) as literals — show only the plain English descriptions mapped to those positions.
- Keep all text labels short (3–6 words); break longer phrases across two lines rather than truncating.

### Integration Mapping for your App

When your application triggers this prompt, map your prototype sentence as follows:

| Variable | Prototype Element | Location |
| :--- | :--- | :--- |
| **[LOOP_NAME_CAPS]** | The "Loop Name" | Title bar + Z badge center |
| **[NARRATIVE_1_TEXT]** | **[X]** (User Action) | Left panel scene subject |
| **[NARRATIVE_2_TEXT]** | **[Y]** (User Receives) | Middle reward box |
| **[NARRATIVE_3_TEXT]** | The "Loop Action" | Right panel circle stages (derived) |
| **[NARRATIVE_4_TEXT]** | **[Z]** (Producer Closes) | Right panel circle stages (derived) |