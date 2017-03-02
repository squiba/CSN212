(TeX-add-style-hook
 "corman"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem")))
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "inputenc"
    "fontenc"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref")
   (LaTeX-add-labels
    "sec:orgee23445"
    "sec:orgb370f73"
    "sec:orge60101e"
    "sec:orgcc5e894"
    "sec:org1523936"
    "sec:org1777c67"
    "sec:org171b1db"
    "sec:org316d8c3"
    "sec:org6984e1c"
    "sec:orge7e9b86"
    "sec:orgdfcff68"
    "sec:orgbbd09bd"
    "sec:orgc07c923"
    "sec:orgb640a25"
    "sec:org94f0912"
    "sec:org92a7881"
    "sec:org0d309ac"
    "sec:orgd682bef"
    "sec:org10c0b3e"
    "sec:org1cff466"
    "sec:org7024021"))
 :latex)

