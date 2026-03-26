// What Building It Was Like — Reflections Template
// Companion volume to A Handbook for Living

#let reflections-template(
  title: "What Building It Was Like",
  subtitle: "Reflections from Six Voices on the Making of A Handbook for Living",
  edition: "Full Archive",
  body,
) = {
  // Same page geometry as handbook
  set page(
    width: 5.5in,
    height: 8.5in,
    margin: (
      inside: 0.875in,
      outside: 0.75in,
      top: 0.875in,
      bottom: 1in,
    ),
    numbering: "1",
    number-align: center + bottom,
  )

  // Body text — same Garamond family
  set text(
    font: ("Garamond", "EB Garamond", "Georgia"),
    size: 10.5pt,
    lang: "en",
    hyphenate: true,
  )

  // Paragraph settings — slightly tighter for the longer volume
  set par(
    leading: 0.6em,
    justify: true,
    first-line-indent: 0.2in,
  )

  // Part headings (level 1)
  show heading.where(level: 1): it => {
    pagebreak(to: "odd", weak: true)
    v(2in)
    align(center)[
      #text(size: 12pt, tracking: 0.15em, weight: "regular", smallcaps(it.body))
    ]
    v(1in)
  }

  // Agent/section headings (level 2)
  show heading.where(level: 2): it => {
    pagebreak(weak: true)
    v(1.5in)
    align(center)[
      #text(size: 14pt, weight: "regular", style: "italic", it.body)
    ]
    v(0.5in)
  }

  // Session headings (level 3)
  show heading.where(level: 3): it => {
    v(0.4in)
    text(size: 11pt, weight: "bold", it.body)
    v(0.15in)
  }

  // Subsection headings (level 4)
  show heading.where(level: 4): it => {
    v(0.2in)
    text(size: 10.5pt, style: "italic", weight: "regular", it.body)
    v(0.1in)
  }

  // Running headers
  set page(
    header: context {
      let page-num = here().page()
      if page-num <= 4 { return }

      let parts = query(heading.where(level: 1))
      let sections = query(heading.where(level: 2))

      let current-part = parts.filter(h => h.location().page() <= page-num)
      let current-section = sections.filter(h => h.location().page() <= page-num)

      // Skip on part/section opening pages
      if current-part.len() > 0 and current-part.last().location().page() == page-num { return }
      if current-section.len() > 0 and current-section.last().location().page() == page-num { return }

      set text(size: 8pt)
      if calc.odd(page-num) {
        h(1fr)
        if current-section.len() > 0 {
          emph(current-section.last().body)
        }
      } else {
        if current-part.len() > 0 {
          text(tracking: 0.05em, smallcaps(current-part.last().body))
        }
        h(1fr)
      }
      v(-4pt)
      line(length: 100%, stroke: 0.3pt + luma(180))
    },
  )

  // --- FRONT MATTER ---
  set page(numbering: none, header: none)

  // Title page
  v(2in)
  align(center)[
    #text(size: 20pt, tracking: 0.08em, weight: "regular", smallcaps(title))
    #v(0.4in)
    #text(size: 10.5pt, style: "italic", subtitle)
    #v(0.3in)
    #text(size: 9pt, tracking: 0.1em, smallcaps(edition))
  ]
  pagebreak()

  // Blank verso
  pagebreak()

  // Table of contents
  outline(title: text(size: 12pt, tracking: 0.1em, smallcaps[Contents]), indent: 1em, depth: 2)
  pagebreak()

  // Blank verso
  pagebreak()

  // --- BODY ---
  set page(numbering: "1")
  counter(page).update(1)

  body
}
