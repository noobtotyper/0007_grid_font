import cairo
import math

# between 0 and 1/4 to see connections
# between 0 and 1/10 to see protodiagonal and short diagonal separately

class SymbolDrawerSmooth:
    def __init__(self,junction_length=1/20,corners=True, rgb=(0, 0, 0), bg=(0, 0, 0, 0)):
        self.junction_length=junction_length
        self.a = junction_length
        self.s = 0.5-junction_length
        self.d = 0.5+junction_length
        self.f = 1-junction_length
        self.corners=corners
        self.rgb=rgb
        self.bg=bg
    
    def change_junction_length(self,junction_length=1/20):
        """
        0 < junction_lenght < 1/10 is best (protodiagonal and short diagonal separate)
        0 < junction_lenght < 1/4 is bad but readable
        0 <= junction_lenght <= 1 is allowed
        """
        assert type(junction_length)==float and 0<=junction_length<=1
        self.junction_length=junction_length
    
    def change_corners(self,corners=True):
        """change_corners(True) or change_corners(False)"""
        assert type(corners)==bool
        self.corners=corners
    
    def change_rgb(self,rgb = (0,0,0)):
        """change_rgb((1,0,0.8))"""
        assert type(rgb)==tuple and len(rgb)==3
        self.rgb=rgb
    
    def change_bg(self,bg= (0,0,0,0)):
        """change_bg((0,0,0,0))
        Last value of 0 means transparent, 1 means opaque"""
        assert type(bg)==tuple and len(bg)==4
        self.bg=bg
    
    ## straight
    # 2 long straight
    def t_b(self, cr: cairo.Context):
        cr.move_to(self.s, 0)
        cr.line_to(self.d, 0)
        cr.line_to(self.d, 1)
        cr.line_to(self.s, 1)
        cr.close_path()
        cr.fill()
    def l_r(self, cr: cairo.Context):
        cr.move_to(0, self.s)
        cr.line_to(0, self.d)
        cr.line_to(1, self.d)
        cr.line_to(1, self.s)
        cr.close_path()
        cr.fill()

    ## 4 short straight
    def t_c(self, cr: cairo.Context):
        cr.move_to(self.s, 0)
        cr.line_to(self.d, 0)
        cr.line_to(self.d, self.d)
        cr.line_to(self.s, self.d)
        cr.close_path()
        cr.fill()
    def l_c(self, cr: cairo.Context):
        cr.move_to(0, self.s)
        cr.line_to(0, self.d)
        cr.line_to(self.d, self.d)
        cr.line_to(self.d, self.s)
        cr.close_path()
        cr.fill()
    def b_c(self, cr: cairo.Context):
        cr.move_to(self.s, self.s)
        cr.line_to(self.d, self.s)
        cr.line_to(self.d, 1)
        cr.line_to(self.s, 1)
        cr.close_path()
        cr.fill()
    def r_c(self, cr: cairo.Context):
        cr.move_to(self.s, self.s)
        cr.line_to(self.s, self.d)
        cr.line_to(1, self.d)
        cr.line_to(1, self.s)
        cr.close_path()
        cr.fill()


    ## diagonals
    # 2 long diagonals
    def tl_br(self, cr: cairo.Context):
        cr.move_to(0, 0)
        cr.line_to(self.a, 0)
        cr.line_to(1, self.f)
        cr.line_to(1, 1)
        cr.line_to(self.f, 1)
        cr.line_to(0, self.a)
        cr.close_path()
        cr.fill()
    def tr_bl(self, cr: cairo.Context):
        cr.move_to(self.f, 0)
        cr.line_to(1, 0)
        cr.line_to(1, self.a)
        cr.line_to(self.a, 1)
        cr.line_to(0, 1)
        cr.line_to(0, self.f)
        cr.close_path()
        cr.fill()

    # 8 short diagonals
    def tl_c(self, cr: cairo.Context):
        cr.move_to(0, self.a)
        cr.line_to(0, 0)
        cr.line_to(self.a, 0)
        cr.line_to(self.d, self.s)
        cr.line_to(self.d, self.d)
        cr.line_to(self.s, self.d)
        cr.close_path()
        cr.fill()
    def tr_c(self, cr: cairo.Context):
        cr.move_to(self.f, 0)
        cr.line_to(1, 0)
        cr.line_to(1, self.a)
        cr.line_to(self.d, self.d)
        cr.line_to(self.s, self.d)
        cr.line_to(self.s, self.s)
        cr.close_path()
        cr.fill()
    def bl_c(self, cr: cairo.Context):
        cr.move_to(self.a, 1)
        cr.line_to(0, 1)
        cr.line_to(0, self.f)
        cr.line_to(self.s, self.s)
        cr.line_to(self.d, self.s)
        cr.line_to(self.d, self.d)
        cr.close_path()
        cr.fill()
    def br_c(self, cr: cairo.Context):
        cr.move_to(1, self.f)
        cr.line_to(1, 1)
        cr.line_to(self.f, 1)
        cr.line_to(self.s, self.d)
        cr.line_to(self.s, self.s)
        cr.line_to(self.d, self.s)
        cr.close_path()
        cr.fill()
    def t_l(self, cr: cairo.Context):
        cr.move_to(self.s, 0)
        cr.line_to(self.d, 0)
        cr.line_to(0, self.d)
        cr.line_to(0, self.s)
        cr.close_path()
        cr.fill()
    def t_r(self, cr: cairo.Context):
        cr.move_to(self.s, 0)
        cr.line_to(self.d, 0)
        cr.line_to(1, self.s)
        cr.line_to(1, self.d)
        cr.close_path()
        cr.fill()
    def b_l(self, cr: cairo.Context):
        cr.move_to(self.d, 1)
        cr.line_to(self.s, 1)
        cr.line_to(0, self.d)
        cr.line_to(0, self.s)
        cr.close_path()
        cr.fill()
    def b_r(self, cr: cairo.Context):
        cr.move_to(self.d, 1)
        cr.line_to(self.s, 1)
        cr.line_to(1, self.s)
        cr.line_to(1, self.d)
        cr.close_path()
        cr.fill()

    ## 8 protodiagonals
    # 4 more vertical
    def t_bl(self, cr: cairo.Context):
        cr.move_to(0, self.f)
        cr.line_to(self.s, 0)
        cr.line_to(self.d, 0)
        cr.line_to(self.a, 1)
        cr.line_to(0, 1)
        cr.close_path()
        cr.fill()
    def t_br(self, cr: cairo.Context):
        cr.move_to(1, self.f)
        cr.line_to(1, 1)
        cr.line_to(self.f, 1)
        cr.line_to(self.s, 0)
        cr.line_to(self.d, 0)
        cr.close_path()
        cr.fill()
    def b_tl(self, cr: cairo.Context):
        cr.move_to(0, 0)
        cr.line_to(self.a, 0)
        cr.line_to(self.d, 1)
        cr.line_to(self.s, 1)
        cr.line_to(0, self.a)
        cr.close_path()
        cr.fill()
    def b_tr(self, cr: cairo.Context):
        cr.move_to(1, 0)
        cr.line_to(1, self.a)
        cr.line_to(self.d, 1)
        cr.line_to(self.s, 1)
        cr.line_to(self.f, 0)
        cr.line_to(0, 0)
        cr.close_path()
        cr.fill()

    # 4 more horizontal
    def r_tl(self, cr: cairo.Context):
        cr.move_to(0, 0)
        cr.line_to(self.a, 0)
        cr.line_to(1, self.s)
        cr.line_to(1, self.d)
        cr.line_to(0, self.a)
        cr.close_path()
        cr.fill()
    def r_bl(self, cr: cairo.Context):
        cr.move_to(0, 1)
        cr.line_to(0, self.f)
        cr.line_to(1, self.s)
        cr.line_to(1, self.d)
        cr.line_to(self.a, 1)
        cr.close_path()
        cr.fill()
    def l_tr(self, cr: cairo.Context):
        cr.move_to(self.f, 0)
        cr.line_to(1, 0)
        cr.line_to(1, self.a)
        cr.line_to(0, self.d)
        cr.line_to(0, self.s)
        cr.close_path()
        cr.fill()
    def l_br(self, cr: cairo.Context):
        cr.move_to(1, self.f)
        cr.line_to(1, 1)
        cr.line_to(self.f, 1)
        cr.line_to(0, self.d)
        cr.line_to(0, self.s)
        cr.close_path()
        cr.fill()


    ## I add all names swapped so that I can draw lines in both directions
    # straight
    def b_t(self, cr: cairo.Context):
        self.t_b(cr)
    def r_l(self, cr: cairo.Context):
        self.l_r(cr)
    def c_t(self, cr: cairo.Context):
        self.t_c(cr)
    def c_l(self, cr: cairo.Context):
        self.l_c(cr)
    def c_b(self, cr: cairo.Context):
        self.b_c(cr)
    def c_r(self, cr: cairo.Context):
        self.r_c(cr)


    # diagonals
    def br_tl(self, cr: cairo.Context):
        self.tl_br(cr)
    def bl_tr(self, cr: cairo.Context):
        self.tr_bl(cr)
    def c_tl(self, cr: cairo.Context):
        self.tl_c(cr)
    def c_tr(self, cr: cairo.Context):
        self.tr_c(cr)
    def c_bl(self, cr: cairo.Context):
        self.bl_c(cr)
    def c_br(self, cr: cairo.Context):
        self.br_c(cr)
    def l_t(self, cr: cairo.Context):
        self.t_l(cr)
    def r_t(self, cr: cairo.Context):
        self.t_r(cr)
    def l_b(self, cr: cairo.Context):
        self.b_l(cr)
    def r_b(self, cr: cairo.Context):
        self.b_r(cr)


    # protodiagonals
    def bl_t(self, cr: cairo.Context):
        self.t_bl(cr)
    def br_t(self, cr: cairo.Context):
        self.t_br(cr)
    def tl_b(self, cr: cairo.Context):
        self.b_tl(cr)
    def tr_b(self, cr: cairo.Context):
        self.b_tr(cr)
    def tl_r(self, cr: cairo.Context):
        self.r_tl(cr)
    def bl_r(self, cr: cairo.Context):
        self.r_bl(cr)
    def tr_l(self, cr: cairo.Context):
        self.l_tr(cr)
    def br_l(self, cr: cairo.Context):
        self.l_br(cr)

    def fill_corners(self, cr: cairo.Context):
        # top left
        cr.move_to(0, 0)
        cr.line_to(self.a, 0)
        cr.line_to(0, self.a)
        cr.close_path()

        # top right
        cr.move_to(self.f, 0)
        cr.line_to(1, 0)
        cr.line_to(1, self.a)
        cr.close_path()

        # bottom right
        cr.move_to(1, self.f)
        cr.line_to(1, 1)
        cr.line_to(self.f, 1)
        cr.close_path()

        # bottom left
        cr.move_to(self.a, 1)
        cr.line_to(0, 1)
        cr.line_to(0, self.f)
        cr.close_path()

        cr.fill()
    
    def fill_symbol(self, cr: cairo.Context, symbol):
        match symbol:
            case "a":
                self.t_bl(cr)
                self.t_br(cr)
            case "b":
                self.tl_c(cr)
                self.l_r(cr)
                self.bl_r(cr)
            case "c":
                self.tr_l(cr)
                self.l_br(cr)
            case "d":
                self.tl_r(cr)
                self.r_bl(cr)
            case "e":
                self.tr_l(cr)
                self.l_br(cr)
                self.l_r(cr)
            case "f":
                self.l_r(cr)
                self.bl_t(cr)
            case "g":
                self.tr_l(cr)
                self.l_br(cr)
                self.c_br(cr)
            case "h":
                self.t_bl(cr)
                self.bl_c(cr)
                self.c_br(cr)
            case "i":
                self.t_b(cr)
            case "j":
                self.t_br(cr)
                self.br_l(cr)
            case "k":
                self.t_b(cr)
                self.tr_l(cr)
                self.l_br(cr)
            case "l":
                self.t_b(cr)
                self.b_r(cr)
            case "m":
                self.bl_t(cr)
                self.t_b(cr)
                self.t_br(cr)
            case "n":
                self.tl_br(cr)
            case "ñ":
                self.tl_br(cr)
                self.t_r(cr)
            case "o":
                self.t_r(cr)
                self.t_l(cr)
                self.b_r(cr)
                self.b_l(cr)
            case "p":
                self.b_tl(cr)
                self.tl_r(cr)
                self.r_l(cr)
            case "q":
                self.t_r(cr)
                self.t_l(cr)
                self.b_r(cr)
                self.b_l(cr)
                self.c_br(cr)
            case "r":
                self.tl_r(cr)
                self.r_l(cr)
                self.l_br(cr)
            case "s":
                self.t_l(cr)
                self.l_r(cr)
                self.r_b(cr)
            case "t":
                self.t_b(cr)
                self.l_r(cr)
            case "u":
                self.tl_b(cr)
                self.b_tr(cr)
                self.c_br(cr)
            case "v":
                self.tl_b(cr)
                self.b_tr(cr)
            case "w":
                self.tl_b(cr)
                self.t_b(cr)
                self.tr_b(cr)
            case "x":
                self.tl_br(cr)
                self.tr_bl(cr)
            case "y":
                self.tl_c(cr)
                self.tr_c(cr)
                self.c_b(cr)
            case "z":
                self.tr_bl(cr)
            case "0":
                self.t_l(cr)
                self.l_b(cr)
                self.b_r(cr)
                self.r_t(cr)
                self.tr_bl(cr)
            case "1":
                self.l_t(cr)
                self.t_b(cr)
            case "2":
                self.l_tr(cr)
                self.tr_bl(cr)
                self.bl_r(cr)
            case "3":
                self.tl_r(cr)
                self.l_r(cr)
                self.bl_r(cr)
            case "4":
                self.b_t(cr)
                self.t_l(cr)
                self.l_r(cr)
            case "5":
                self.r_tl(cr)
                self.tl_br(cr)
                self.br_l(cr)
            case "6":
                self.tr_l(cr)
                self.l_b(cr)
                self.b_r(cr)
                self.r_l(cr)
            case "7":
                self.l_tr(cr)
                self.tr_b(cr)
                self.c_r(cr)
            case "8":
                self.t_l(cr)
                self.l_b(cr)
                self.b_r(cr)
                self.r_t(cr)
                self.l_r(cr)
            case "9":
                self.t_l(cr)
                self.l_r(cr)
                self.r_t(cr)
                self.bl_r(cr)
            case "´":  # _accent_acute
                self.l_t(cr)
            case "`":  # _accent_grave
                self.tl_c(cr)
            case "&":  # _ampersand
                self.t_b(cr)
                self.b_l(cr)
                self.l_t(cr)
                self.l_r(cr)
                self.c_br(cr)
            case "'":  # _apostrophe
                self.t_c(cr)
            case "*":  # _asterisk
                self.tl_r(cr)
                self.l_tr(cr)
                self.t_c(cr)
            case "@":  # _at
                self.l_r(cr)
                self.r_bl(cr)
                self.bl_t(cr)
                self.t_br(cr)
            case "\\":  # _backslash
                self.tl_b(cr)
            case "{":  # _bracket_l
                self.tr_c(cr)
                self.br_c(cr)
                self.l_c(cr)
            case "}":  # _bracket_r
                self.tl_c(cr)
                self.bl_c(cr)
                self.r_c(cr)
            case "^":  # _caret
                self.l_t(cr)
                self.t_r(cr)
            case "ˇ":  # _caron
                self.tl_c(cr)
                self.c_tr(cr)
            case "¸":  # _cedilla
                self.c_b(cr)
            case "ç":  # _cedilla_c
                self.tr_l(cr)
                self.l_br(cr)
                self.c_b(cr)
            case ":":  # _colon
                self.tl_c(cr)
                self.c_bl(cr)
                self.t_l(cr)
                self.l_b(cr)
            case ",":  # _comma
                self.c_bl(cr)
            case "¤":  # _currency
                self.tl_br(cr)
                self.bl_tr(cr)
                self.t_l(cr)
                self.l_b(cr)
                self.b_r(cr)
                self.r_t(cr)
            case "-":  # _dash
                self.l_c(cr)
            case "°":  # _degree
                self.tl_c(cr)
                self.t_l(cr)
            case "$":  # _dollar
                self.t_l(cr)
                self.l_r(cr)
                self.r_b(cr)
                self.tl_br(cr)
            case "·":  # _dot
                cr.move_to(self.s,self.s)
                cr.line_to(self.d,self.s)
                cr.line_to(self.d,self.d)
                cr.line_to(self.s,self.d)
                cr.close_path()
                cr.fill()
            case "«":  # _double_angle_l
                self.t_l(cr)
                self.l_b(cr)
                self.r_c(cr)
                self.c_br(cr)
            case "»":  # _double_angle_r
                self.t_r(cr)
                self.r_b(cr)
                self.l_c(cr)
                self.c_bl(cr)
            case "—":  # _em_dash
                cr.move_to(1,self.s)
                cr.line_to(1,self.d)
                cr.line_to(0.25,self.d)
                cr.line_to(0.25,self.s)
                cr.close_path()
                cr.fill()
            case "–":  # _en_dash
                self.c_r(cr)
            # TODO
            case "=":  # _equal
                cr.move_to(0.25, 0.25)
                cr.line_to(0.75, 0.25)
                cr.line_to(0.75, 0.25+2*self.junction_length)
                cr.line_to(0.25, 0.25+2*self.junction_length)
                cr.close_path()
                cr.move_to(0.75,0.75)
                cr.line_to(0.25,0.75)
                cr.line_to(0.25,0.75-2*self.junction_length)
                cr.line_to(0.75,0.75-2*self.junction_length)
                cr.close_path()
                cr.fill()
            case "€":  # _euro
                self.l_tr(cr)
                self.l_r(cr)
                self.l_br(cr)
                self.t_b(cr)
            case "ß": # _eszett
                self.t_l(cr)
                self.l_r(cr)
                self.r_b(cr)
                self.tr_bl(cr)
            case "¡":  # _exclamation_l
                self.b_c(cr)
                self.c_tl(cr)
                self.l_t(cr)
            case "!":  # _exclamation_r
                self.t_c(cr)
                self.c_bl(cr)
                self.l_b(cr)
            case ">":  # _greaterthan
                self.l_c(cr)
                self.c_bl(cr)
            case "#":  # _hashtag
                self.bl_t(cr)
                self.b_tr(cr)
                self.tl_r(cr)
                self.l_br(cr)
            case "<":  # _lessthan
                self.r_c(cr)
                self.c_br(cr)
            case "−":  # _minus
                cr.move_to(0.25,self.s)
                cr.line_to(0.75,self.s)
                cr.line_to(0.75,self.d)
                cr.line_to(0.25,self.d)
                cr.close_path()
                cr.fill()
            case "×":  # _multiplication
                cr.move_to(0.25, 0.25)
                cr.line_to(0.75, 0.75)
                cr.move_to(0.75, 0.25)
                cr.line_to(0.25, 0.75)
                cr.set_line_width(self.junction_length*math.sqrt(2))
                cr.stroke()
            case "¬":  # _not
                self.l_c(cr)
                self.c_b(cr)
            case "(":  # _parenthesis_l
                self.tr_c(cr)
                self.c_br(cr)
            case ")":  # _parenthesis_r
                self.tl_c(cr)
                self.c_bl(cr)
            case "%":  # _percentage
                self.tl_br(cr)
                self.l_t(cr)
                self.b_r(cr)
                self.bl_tr(cr)
            case ".":  # _period
                self.l_b(cr)
                self.bl_c(cr)
            case "+":  # _plus
                cr.move_to(0.25, self.s)
                cr.line_to(0.75, self.s)
                cr.line_to(0.75, self.d)
                cr.line_to(0.25, self.d)
                cr.close_path()
                cr.fill()
                cr.move_to(self.s,0.25)
                cr.line_to(self.s,0.75)
                cr.line_to(self.d,0.75)
                cr.line_to(self.d,0.25)
                cr.close_path()
                cr.fill()
            case "£":  # _pound
                self.t_b(cr)
                self.b_r(cr)
                self.bl_tr(cr)
            case "¿":  # _question_l
                self.t_c(cr)
                self.c_l(cr)
                self.l_b(cr)
            case "?":  # _question_r
                self.t_r(cr)
                self.r_c(cr)
                self.c_b(cr)
            case '"':  # _quotation
                self.l_t(cr)
                self.c_tr(cr)
            case "⏎": # _ return
                self.t_c(cr)
                self.l_c(cr)
            case ";":  # _semicolon
                self.tl_c(cr)
                self.l_t(cr)
                self.c_bl(cr)
            case "/":  # _slash
                self.t_bl(cr)
            case " ":  # _space
                pass
            case "[":  # _squarebracket_l
                self.t_b(cr)
                self.l_c(cr)
            case "]":  # _squarebracket_r
                self.t_b(cr)
                self.c_r(cr)
            case "⭾":  # _tab
                self.tl_c(cr)
                self.t_b(cr)
                self.l_c(cr)
                self.bl_c(cr)
            case "~":  # _tilde
                self.tl_c(cr)
                self.c_t(cr)
                self.t_r(cr)
            case "¨":  # _umlaut
                self.tl_c(cr)
                self.c_tr(cr)
                self.l_t(cr)
                self.t_r(cr)
            case "_":  # _underscore
                self.l_r(cr)
            case "|":  # _vertical
                cr.move_to(self.s,0.25)
                cr.line_to(self.s,0.75)
                cr.line_to(self.d,0.75)
                cr.line_to(self.d,0.25)
                cr.close_path()
                cr.fill()

            case default:
                return

        # TODO redundant
        cr.fill()


    def draw_symbol(self, cr: cairo.Context, symbol, line_width=0.01):

        cr.set_source_rgba(self.bg[0], self.bg[1], self.bg[2], self.bg[3])
        cr.rectangle(0, 0, 1, 1)
        cr.fill()

        cr.set_line_width(line_width)
        cr.set_source_rgb(self.rgb[0], self.rgb[1], self.rgb[2])
        self.fill_symbol(cr, symbol)
        if self.corners:
            self.fill_corners(cr)