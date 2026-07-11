"""``postal`` — postal / ZIP code shape (accepts any known locale)."""

from __future__ import annotations

from edify import Pattern, any_of

_digit3 = Pattern().exactly(3).digit()
_digit4 = Pattern().exactly(4).digit()
_digit5 = Pattern().exactly(5).digit()
_digit6 = Pattern().exactly(6).digit()
_digit7 = Pattern().exactly(7).digit()

_alnum_upper = Pattern().any_of().range("A", "Z").range("0", "9").end()

_prefix_120_or_122 = (
    Pattern().group().any_of().string("120").string("122").end().end().exactly(2).digit()
)

_netherlands = (
    Pattern()
    .optional()
    .group()
    .string("NL-")
    .end()
    .exactly(4)
    .digit()
    .zero_or_more()
    .whitespace_char()
    .exactly(2)
    .uppercase()
)

_eircode_prefix = (
    Pattern()
    .any_of()
    .char("A")
    .range("C", "F")
    .char("H")
    .char("K")
    .char("N")
    .char("P")
    .char("R")
    .char("T")
    .range("V", "Y")
    .end()
    .exactly(2)
    .digit()
)
_eircode = (
    Pattern()
    .group()
    .any_of()
    .subexpression(_eircode_prefix)
    .string("D6W")
    .end()
    .end()
    .optional()
    .any_of_chars(" -")
    .exactly(4)
    .any_of()
    .range("0", "9")
    .char("A")
    .range("C", "F")
    .char("H")
    .char("K")
    .char("N")
    .char("P")
    .char("R")
    .char("T")
    .range("V", "Y")
    .end()
)

_uk_gir = Pattern().string("GIR 0AA")

_uk_alpha_upper_lower = Pattern().any_of().range("A", "Z").range("a", "z").end()
_uk_alpha_no_ilo_upper_lower = (
    Pattern().any_of().range("A", "H").range("J", "Y").range("a", "h").range("j", "y").end()
)

_uk_outward = any_of(
    Pattern().subexpression(_uk_alpha_upper_lower).between(1, 2).digit(),
    Pattern()
    .subexpression(_uk_alpha_upper_lower)
    .subexpression(_uk_alpha_no_ilo_upper_lower)
    .between(1, 2)
    .digit(),
    Pattern().subexpression(_uk_alpha_upper_lower).digit().subexpression(_uk_alpha_upper_lower),
    Pattern()
    .subexpression(_uk_alpha_upper_lower)
    .subexpression(_uk_alpha_no_ilo_upper_lower)
    .digit()
    .optional()
    .subexpression(_uk_alpha_upper_lower),
)

_uk_full = (
    Pattern()
    .subexpression(_uk_outward)
    .optional()
    .whitespace_char()
    .digit()
    .exactly(2)
    .subexpression(_uk_alpha_upper_lower)
)

_uk = any_of(_uk_gir, _uk_full)

_lit_96950 = Pattern().string("96950")
_prefix_971 = Pattern().string("971").exactly(2).digit()
_prefix_972 = Pattern().string("972").exactly(2).digit()
_prefix_973 = Pattern().string("973").exactly(2).digit()
_prefix_974 = Pattern().string("974").exactly(2).digit()
_prefix_976 = Pattern().string("976").exactly(2).digit()
_prefix_980 = Pattern().string("980").exactly(2).digit()
_prefix_987 = Pattern().string("987").exactly(2).digit()
_prefix_988 = Pattern().string("988").exactly(2).digit()

_ai_2640 = Pattern().string("AI-2640")
_bb_plus_5 = Pattern().string("BB").exactly(5).digit()
_fiqq = Pattern().string("FIQQ 1ZZ")
_gx11 = Pattern().string("GX11 1AA")
_lt_5 = Pattern().string("LT-").exactly(5).digit()
_lv_4 = Pattern().string("LV-").exactly(4).digit()
_md_4 = Pattern().string("MD").optional().char("-").exactly(4).digit()
_msr_4 = Pattern().string("MSR ").exactly(4).digit()
_sthl = Pattern().string("STHL 1ZZ")
_tkca = Pattern().string("TKCA 1ZZ")
_vc_4 = Pattern().string("VC").exactly(4).digit()
_vg_4 = Pattern().string("VG").exactly(4).digit()
_ws_4 = Pattern().string("WS").exactly(4).digit()

_2_dash_3 = Pattern().exactly(2).digit().char("-").exactly(3).digit()
_3_sp_2 = Pattern().exactly(3).digit().whitespace_char().exactly(2).digit()
_3_opt_dash_2 = Pattern().exactly(3).digit().optional().group().char("-").exactly(2).digit().end()
_3_dash_4 = Pattern().exactly(3).digit().char("-").exactly(4).digit()
_4_sp_4 = Pattern().exactly(4).digit().whitespace_char().exactly(4).digit()
_4_opt_dash_letter = Pattern().exactly(4).digit().optional().group().char("-").uppercase().end()
_4_dash_3 = Pattern().exactly(4).digit().char("-").exactly(3).digit()
_5_opt_dash_4 = Pattern().exactly(5).digit().optional().group().char("-").exactly(4).digit().end()
_5_dash_3 = Pattern().exactly(5).digit().char("-").exactly(3).digit()
_5_or_7 = any_of(_digit5, _digit7)

_ca = (
    Pattern()
    .uppercase()
    .digit()
    .uppercase()
    .optional()
    .whitespace_char()
    .digit()
    .uppercase()
    .digit()
)
_upper1_digit3 = Pattern().uppercase().exactly(3).digit()
_upper1_digit4_upper3 = Pattern().uppercase().exactly(4).digit().exactly(3).uppercase()
_upper2_sp_digit5 = Pattern().exactly(2).uppercase().whitespace_char().exactly(5).digit()
_upper2_digit1_dash_digit4 = Pattern().exactly(2).uppercase().digit().char("-").exactly(4).digit()
_upper2_digit2_sp_digit3 = (
    Pattern().exactly(2).uppercase().exactly(2).digit().whitespace_char().exactly(3).digit()
)
_upper2_digit2 = Pattern().exactly(2).uppercase().exactly(2).digit()
_upper2_digit4 = Pattern().exactly(2).uppercase().exactly(4).digit()
_upper3_sp_digit4 = Pattern().exactly(3).uppercase().whitespace_char().exactly(4).digit()

_us_dash_or_space = (
    Pattern()
    .exactly(5)
    .digit()
    .optional()
    .group()
    .any_of_chars("-")
    .subexpression(Pattern().any_of().char("-").whitespace_char().end())
    .exactly(4)
    .digit()
    .end()
)

_india = Pattern().assert_not_ahead().char("0").end().exactly(6).digit()

_all_locales = any_of(
    _prefix_120_or_122,
    _netherlands,
    _eircode,
    _uk,
    _lit_96950,
    _prefix_971,
    _prefix_972,
    _prefix_973,
    _prefix_974,
    _prefix_976,
    _prefix_980,
    _prefix_987,
    _prefix_988,
    _ai_2640,
    _bb_plus_5,
    _fiqq,
    _gx11,
    _lt_5,
    _lv_4,
    _md_4,
    _msr_4,
    _sthl,
    _tkca,
    _vc_4,
    _vg_4,
    _ws_4,
    _2_dash_3,
    _3_sp_2,
    _digit3,
    _3_opt_dash_2,
    _3_dash_4,
    _4_sp_4,
    _digit4,
    _4_opt_dash_letter,
    _4_dash_3,
    _digit5,
    _5_opt_dash_4,
    _5_dash_3,
    _5_or_7,
    _digit6,
    _digit7,
    _ca,
    _upper1_digit3,
    _upper1_digit4_upper3,
    _upper2_sp_digit5,
    _upper2_digit1_dash_digit4,
    _upper2_digit2_sp_digit3,
    _upper2_digit2,
    _upper2_digit4,
    _upper3_sp_digit4,
    _us_dash_or_space,
    _india,
)

postal = Pattern().start_of_input().subexpression(_all_locales).end_of_input()
"""Callable :class:`Pattern` that accepts any known postal/ZIP shape by locale."""
