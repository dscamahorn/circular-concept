### Circular Image Generation Prompt

**Aspect Ratio:** 16:9

**Style & Brand Identity:**
Generate a professional, flat-lay diagram in a clean **marker sketch style**. The visual language (color palette, line weight, and typography) must strictly follow the specifications outlined in the **DESIGN.md** file. Render the image on a slightly textured, off-white paper background with bold, confident strokes. **Strictly avoid any hands, markers, pens, or people in the frame.**

**Composition:**

1.  **System Title:** At the top center, display: "**[LOOP_NAME_CAPS]**" using the primary font specified in **DESIGN.md**.
2.  **The Central Loop:** The centerpiece is a prominent circular flow diagram. It consists of four colored arrow segments that interlock to form a **continuous clockwise loop**.
3.  **Clockwise Numbered Narrative:** Place four narrative text blocks around the loop. They must follow a strict **clockwise sequence** (starting Top-Left at 1, moving to Top-Right at 2, Bottom-Right at 3, and finishing Bottom-Left at 4).
    * **Node 1 (Top-Left):** Display numeral "**1**" with text: "**[NARRATIVE_1_TEXT]**".
    * **Node 2 (Top-Right):** Display numeral "**2**" with text: "**[NARRATIVE_2_TEXT]**".
    * **Node 3 (Bottom-Right):** Display numeral "**3**" with text: "**[NARRATIVE_3_TEXT]**".
    * **Node 4 (Bottom-Left):** Display numeral "**4**" with text: "**[NARRATIVE_4_TEXT]**".
4.  **AI-Driven Iconography:** For each node, the AI must analyze the text in the `[NARRATIVE_X_TEXT]` variable and generate a corresponding stylized marker-sketch icon that visually represents that specific action or outcome. These icons should be placed inside or immediately adjacent to their respective loop segments.

**Visual Formatting:**
* **Color Mapping:** Use the hex codes from **DESIGN.md** to color-code each segment of the loop and its matching number/text block.
* **Typography:** Use the "Design System" fonts for all labels and headers to ensure brand consistency.
* **Variables:** Do not display variable names (X, Y, Z); show only the number and the plain English description.


