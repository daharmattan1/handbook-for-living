// Handbook for Living — Book Template
// Literary press style: 5.5" x 8.5" trade paperback

#let book-template(
  title: "A Handbook for Living",
  subtitle: "Written by six voices",
  epigraph: none,
  body,
) = {
  // Page geometry
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

  // Body text — Garamond for literary serif
  set text(
    font: ("Garamond", "EB Garamond", "Georgia"),
    size: 11pt,
    lang: "en",
    hyphenate: true,
  )

  // Paragraph settings
  set par(
    leading: 0.636em, // ~15pt leading at 11pt
    justify: true,
    first-line-indent: 0.25in,
  )

  // Widow/orphan control
  set block(breakable: true)

  // Heading styles (chapter titles)
  show heading.where(level: 1): it => {
    // Force chapter start on recto (odd/right) page
    pagebreak(to: "odd", weak: true)

    // Drop from top
    v(2.5in)

    // Chapter title in small caps
    set text(
      size: 16pt,
      weight: "regular",
      tracking: 0.12em,
    )
    align(center, smallcaps(it.body))

    // Space after title
    v(0.75in)

    // Reset first-line indent for first paragraph after heading
    set par(first-line-indent: 0pt)
  }

  // Running headers
  set page(
    header: context {
      let page-num = here().page()
      // No header on chapter-opening pages or front matter
      if page-num <= 6 { return }

      let chapters = query(heading.where(level: 1))
      let matching = chapters.filter(h => h.location().page() <= page-num)
      if matching.len() == 0 { return }
      let current-chapter = matching.last()

      // Skip header if this is a chapter-opening page
      if current-chapter.location().page() == page-num { return }

      set text(size: 8.5pt)
      if calc.odd(page-num) {
        // Recto (right): book title in italics
        h(1fr)
        emph[A Handbook for Living]
      } else {
        // Verso (left): chapter title in small caps
        text(tracking: 0.05em, smallcaps(current-chapter.body))
        h(1fr)
      }
      v(-4pt)
      line(length: 100%, stroke: 0.3pt + luma(180))
    },
  )

  // --- FRONT MATTER ---

  // Half-title page
  set page(numbering: none, header: none)
  v(2.5in)
  align(center, text(size: 18pt, tracking: 0.1em, smallcaps[A Handbook for Living]))
  pagebreak()

  // Blank verso
  pagebreak()

  // Full title page
  v(2in)
  align(center)[
    #text(size: 24pt, tracking: 0.08em, weight: "regular", smallcaps[A Handbook for Living])
    #v(0.3in)
    #text(size: 11pt, style: "italic")[Written by six voices]
  ]
  pagebreak()

  // Blank verso
  pagebreak()

  // Epigraph page
  if epigraph != none {
    v(2in)
    align(center, block(width: 3.5in, text(size: 11pt, style: "italic", epigraph)))
    pagebreak()

    // Blank verso after epigraph
    pagebreak()
  }

  // --- BODY ---
  set page(numbering: "1")
  counter(page).update(1)

  body
}
