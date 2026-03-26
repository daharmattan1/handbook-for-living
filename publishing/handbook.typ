// A Handbook for Living — Master Document
// Compile: typst compile handbook.typ handbook-for-living.pdf

#import "template.typ": book-template

#show: book-template.with(
  title: "A Handbook for Living",
  subtitle: "Written by six voices",
  epigraph: [There is something in a man that recognizes before it is taught.],
)

#include "chapters/01_loss.typ"
#include "chapters/02_tuesday.typ"
#include "chapters/03_commute.typ"
#include "chapters/04_glass.typ"
#include "chapters/05_cup.typ"
#include "chapters/06_morning.typ"
