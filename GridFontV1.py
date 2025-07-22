import math

import cairo
from io import BytesIO
from lxml import etree

def disp_and_save(
    draw_func,
    symbol,
    display=False,
    folder="IconsV1/",
    filename_png=None,
    filename_svg=None,
    res=256,
    line_width=0.1,
    rgb=(0,0,0),
    bg=(0,0,0,0)
):
    width = res
    height = res


    # Create an ImageSurface for PNG display
    surface_png = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx_png = cairo.Context(surface_png)
    draw_func(ctx_png, symbol, res, line_width=line_width, rgb=rgb, bg=bg)

    if filename_png:
        surface_png.write_to_png(folder + "PNG/" + filename_png + ".png")

    if filename_svg:
        # Create an SVGSurface to save the image as SVG
        surface_svg = cairo.SVGSurface(
            folder + "SVG/" + filename_svg + ".svg", width, height
        )
        ctx_svg = cairo.Context(surface_svg)
        draw_func(ctx_svg, symbol, res, line_width=line_width, rgb=rgb, bg=bg)
        surface_svg.finish()

    if display:  # Display using matplotlib
        with BytesIO() as fileobj:
            import matplotlib.pyplot as plt
            import matplotlib.image as mpimg

            surface_png.write_to_png(fileobj)

            fileobj.seek(0)
            img = mpimg.imread(fileobj, format="png")

            plt.imshow(img)
            plt.axis("off")
            plt.show()

def fill_center(cr: cairo.Context,sq_semiwidth):
    c=0.5
    cr.rectangle(c-sq_semiwidth,c-sq_semiwidth,2*sq_semiwidth,2*sq_semiwidth)
    cr.fill()
    
def stroke_symbol(cr: cairo.Context, symbol, line_width):
    c=0.5
    match symbol:
        case "a":
            cr.move_to(0, 1)
            cr.line_to(c, 0)
            cr.line_to(1, 1)
        case "b":
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.move_to(0,c)
            cr.line_to(1,c)
            cr.line_to(0,1)
        case "c":
            cr.move_to(1, 0)
            cr.line_to(0, c)
            cr.line_to(1, 1)
        case "d":
            cr.move_to(0, 0)
            cr.line_to(1, c)
            cr.line_to(0, 1)
        case "e":
            cr.move_to(1,0)
            cr.line_to(0,c)
            cr.line_to(1,c)
            cr.move_to(0,c)
            cr.line_to(1,1)
        case "f":
            cr.move_to(0, c)
            cr.line_to(1,c)
            cr.move_to(0, 1)
            #cr.line_to(c, 0) #leaves gap, similarly onwards
            cr.line_to(1,-1)
        case "g":
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(1,0)
            cr.line_to(0,c)
            cr.line_to(1,1)
            cr.line_to(c,c)
        case "h":
            cr.move_to(1, -1)
            cr.line_to(0, 1)
            cr.line_to(c, c)
            cr.line_to(1, 1)
        case "i":
            cr.move_to(c, 0)
            cr.line_to(c, 1)
        case "j":
            cr.move_to(0, -1)
            cr.line_to(1, 1)
            cr.line_to(-1,0)
        case "k":
            cr.move_to(1, 0)
            cr.line_to(0, c)
            cr.line_to(1, 1)
            cr.move_to(c, 0)
            cr.line_to(c, 1)
        case "l":
            cr.move_to(c,0)
            cr.line_to(c, 1)
            cr.line_to(1+c,0)
        case "m":
            cr.move_to(0, 1)
            cr.line_to(c, 0)
            cr.line_to(1, 1)
            cr.move_to(c, 0)
            cr.line_to(c, 1)
        case "n":
            cr.move_to(0, 0)
            cr.line_to(1,1)
        case "ñ":
            cr.move_to(0, 0)
            cr.line_to(1,1)
            cr.move_to(0, -c)
            cr.line_to(1+c,1)
        case "o":
            cr.move_to(c, 0)
            cr.line_to(1,c)
            cr.line_to(c,1)
            cr.line_to(0,c)
            cr.line_to(c,0)
        case "p":
            cr.move_to(0,c)
            cr.line_to(1,c)
            cr.line_to(0,0)
            cr.line_to(1,2)
        case "q":
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(c, 0)
            cr.line_to(1,c)
            cr.line_to(c,1)
            cr.line_to(0,c)
            cr.line_to(c,0)
            cr.move_to(c, c)
            cr.line_to(1,1)
        case "r":
            cr.move_to(0, 0)
            cr.line_to(1,c)
            cr.line_to(0,c)
            cr.line_to(1,1)
        case "s":
            cr.move_to(1, -c)
            cr.line_to(0,c)
            cr.line_to(1,c)
            cr.line_to(0,1+c)
        case "t":
            cr.move_to(0, c)
            cr.line_to(1,c)
            cr.move_to(c, 0)
            cr.line_to(c,1)
        case "u":
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(0,0)
            cr.line_to(c,1)
            cr.line_to(1,0)
            cr.move_to(1,1)
            cr.line_to(c,c)
        case "v":
            cr.move_to(0,0)
            cr.line_to(c,1)
            cr.line_to(1,0)
        case "w":
            cr.move_to(0,0)
            cr.line_to(c,1)
            cr.line_to(1,0)
            cr.move_to(c,0)
            cr.line_to(c,1)
        case "x":
            cr.move_to(0, 0)
            cr.line_to(1,1)
            cr.move_to(1, 0)
            cr.line_to(0,1)
        case "y":
            cr.move_to(0, 0)
            cr.line_to(c,c)
            cr.line_to(1, 0)
            cr.move_to(c,c)
            cr.line_to(c,1)
        case "z":
            cr.move_to(1, 0)
            cr.line_to(0,1)
        
        case "0":
            cr.move_to(c, 0)
            cr.line_to(1,c)
            cr.line_to(c,1)
            cr.line_to(0,c)
            cr.line_to(c,0)
            cr.move_to(1, 0)
            cr.line_to(0,1)
        case "1":
            cr.move_to(-c,1)
            cr.line_to(c,0)
            cr.line_to(c,1)
        case "2":
            cr.move_to(-1,1)
            cr.line_to(1,0)
            cr.line_to(0,1)
            cr.line_to(2,0)
        case "3":
            cr.move_to(0,0)
            cr.line_to(1,c)
            cr.line_to(0,c)
            cr.move_to(1,c)
            cr.line_to(0,1)
        case "4":
            cr.move_to(c,1)
            cr.line_to(c,0)
            cr.line_to(0,c)
            cr.line_to(1,c)
        case "5":
            cr.move_to(2,1)
            cr.line_to(0,0)
            cr.line_to(1,1)
            cr.line_to(-1,0)
        case "6":
            cr.move_to(1,0)
            cr.line_to(0,c)
            cr.line_to(c,1)
            cr.line_to(1,c)
            cr.line_to(0,c)
        case "7":
            cr.move_to(-c,1)
            cr.line_to(c,0)
            cr.line_to(c,1)
            cr.move_to(0,1)
            cr.line_to(c,c)
        case "8":
            cr.move_to(c, 0)
            cr.line_to(1,c)
            cr.line_to(c,1)
            cr.line_to(0,c)
            cr.line_to(c,0)
            cr.move_to(0, c)
            cr.line_to(1,c)
        case "9":
            cr.move_to(0,1)
            cr.line_to(1,c)
            cr.line_to(c,0)
            cr.line_to(0,c)
            cr.line_to(1,c)
        
        case "´": #_accent_acute
            cr.move_to(1,-c)
            cr.line_to(-c,1)
        case "`": #_accent_grave
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(0,0)
            cr.line_to(c,c)
        case "&": #_ampersand
            cr.move_to(0,c)
            cr.line_to(c,0)
            cr.line_to(c,1)
            cr.line_to(0,c)
            cr.line_to(1,c)
            cr.move_to(c,c)
            cr.line_to(1,1)
        case "'": #_apostrophe
            fill_center(cr,line_width/2)
            cr.move_to(c,0)
            cr.line_to(c,c)
        case "*": #_asterisk
            fill_center(cr,line_width/2)
            cr.move_to(0,0)
            cr.line_to(2,1)
            cr.move_to(1,0)
            cr.line_to(-1,1)
            cr.move_to(c,0)
            cr.line_to(c,c)
        case "@": #_at
            cr.move_to(1,1)
            cr.line_to(c,0)
            cr.line_to(0,1)
            cr.line_to(1,c)
            cr.line_to(0,c)
        case "\\": #_backslash
            cr.move_to(0,0)
            cr.line_to(1,2)
        case "{": #_bracket_l
            cr.move_to(1,0)
            cr.line_to(c,c)
            cr.line_to(1,1)
            cr.move_to(c,c)
            cr.line_to(0,c)
        case "}": #_bracket_r
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(0,1)
            cr.move_to(c,c)
            cr.line_to(1,c)
        case "^": #_caret
            cr.move_to(-c,1)
            cr.line_to(c,0)
            cr.line_to(1+c,1)
        case "ˇ": #_caron
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(1,0)
        case ":": #_colon
            cr.move_to(1,-c)
            cr.line_to(0,c)
            cr.line_to(1,1+c)
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(0,1)
        case ",": #_comma
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(0,1)
            cr.line_to(c,c)
        case "-": #_dash
            cr.move_to(0.25,c)
            cr.line_to(0.75,c)
        case "°": #_degree
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.move_to(-c,1)
            cr.line_to(1,-c)
        case "$": #_dollar
            cr.move_to(1, -c)
            cr.line_to(0,c)
            cr.line_to(1,c)
            cr.line_to(0,1+c)
            cr.move_to(0,0)
            cr.line_to(1,1)
        case "=": #_equal
            cr.move_to(1/4,1/3)
            cr.line_to(3/4,1/3)
            cr.move_to(1/4,2/3)
            cr.line_to(3/4,2/3)
        case "€": #_euro
            cr.move_to(1,0)
            cr.line_to(0,c)
            cr.line_to(1,c)
            cr.move_to(0,c)
            cr.line_to(1,1)
            cr.move_to(c,0)
            cr.line_to(c,1)
        case "¡": #_exclamation_l
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(c,1)
            cr.move_to(-c,1)
            cr.line_to(1,-c)
        case "!": #_exclamation_r
            cr.move_to(0,1)
            cr.line_to(c,c)
            cr.line_to(c,0)
            cr.move_to(-c,0)
            cr.line_to(1,1+c)
        case ">": #_greaterthan
            cr.move_to(0,c)
            cr.line_to(c,c)
            cr.line_to(0,1)
        case "#": #_hashtag
            cr.move_to(0,0)
            cr.line_to(2,1)
            cr.move_to(-1,0)
            cr.line_to(1,1)
            cr.move_to(1,-1)
            cr.line_to(0,1)
            cr.move_to(0,2)
            cr.line_to(1,0)
        case "<": #_lessthan
            cr.move_to(1,c)
            cr.line_to(c,c)
            cr.line_to(1,1)
        case "×": #_multiplication
            cr.move_to(0.25,0.25)
            cr.line_to(0.75,0.75)
            cr.move_to(0.75,0.25)
            cr.line_to(0.25,0.75)
        case "(": #_parenthesis_l
            cr.move_to(1,0)
            cr.line_to(c,c)
            cr.line_to(1,1)
        case ")": #_parenthesis_r
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(0,1)
        case "%": #_percentage
            cr.move_to(1,0)
            cr.line_to(0,1)
            cr.move_to(0,0)
            cr.line_to(1,1)
            cr.move_to(-c,1)
            cr.line_to(1,-c)
            cr.move_to(0,1+c)
            cr.line_to(1+c,0)
        case ".": #_period
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(-c,0)
            cr.line_to(1,1+c)
            cr.move_to(0,1)
            cr.line_to(c,c)
        case "+": #_plus
            cr.move_to(0.25,c)
            cr.line_to(0.75,c)
            cr.move_to(c,0.25)
            cr.line_to(c,0.75)
        case "¿": #_question_l
            cr.move_to(c,0)
            cr.line_to(c,c)
            cr.line_to(0,c)
            cr.line_to(1,1+c)
        case "?": #_question_r
            cr.move_to(0,-c)
            cr.line_to(1,c)
            cr.line_to(c,c)
            cr.line_to(c,1)
        case "\"": #_quotation
            fill_center(cr,math.sqrt((line_width/2)**2/2))
            cr.move_to(-c,1)
            cr.line_to(1,-c)
            cr.move_to(1,0)
            cr.line_to(c,c)
        case ";": #_semicolon
            cr.move_to(1,-c)
            cr.line_to(-c,1)
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(0,1)
        case "/": #_slash
            cr.move_to(0,1)
            cr.line_to(1,-1)
        case " ": #_space
            pass
        case "[": #_squarebracket_l
            cr.move_to(c,0)
            cr.line_to(c,1)
            cr.move_to(c,c)
            cr.line_to(0,c)
        case "]": #_squarebracket_r
            cr.move_to(c,0)
            cr.line_to(c,1)
            cr.move_to(c,c)
            cr.line_to(1,c)
        case "~": #_tilde
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(c,0)
            cr.line_to(1+c,1)
        case "¨": #_umlaut
            cr.move_to(0,0)
            cr.line_to(c,c)
            cr.line_to(1,0)
            cr.move_to(-c,1)
            cr.line_to(c,0)
            cr.line_to(1+c,1)
        case "_": #_underscore
            cr.move_to(0,c)
            cr.line_to(1,c)
        case "|": #_vertical
            cr.move_to(c,0.25)
            cr.line_to(c,0.75)
        
        case default:
            return
    
    cr.stroke()

def draw_symbol(cr: cairo.Context, symbol, res=256, line_width=0.01, rgb=(0,0,0), bg=(0,0,0,0)):
    cr.scale(res,res)
    
    cr.set_source_rgba(bg[0],bg[1],bg[2],bg[3])
    cr.rectangle(0,0,1,1)
    cr.fill()
    
    cr.set_line_width(line_width)
    cr.set_source_rgb(rgb[0], rgb[1], rgb[2])
    stroke_symbol(cr, symbol, line_width)


symbolnames={symbol:symbol for symbol in "abcdefghijklmnñopqrstuvwxyz0123456789"}
def add_symbols():
    symbolnames[" "]="_space"
    symbolnames["-"]="_dash"
    symbolnames["_"]="_underscore"
    symbolnames["."]="_period"
    symbolnames[","]="_comma"
    symbolnames[":"]="_colon"
    symbolnames[";"]="_semicolon"
    symbolnames["¿"]="_question_l"
    symbolnames["?"]="_question_r"
    symbolnames["¡"]="_exclamation_l"
    symbolnames["!"]="_exclamation_r"

    symbolnames["'"]="_apostrophe"
    symbolnames["\""]="_quotation"
    symbolnames["´"]="_accent_acute"
    symbolnames["`"]="_accent_grave"
    symbolnames["/"]="_slash"
    symbolnames["\\"]="_backslash"

    symbolnames["("]="_parenthesis_l"
    symbolnames[")"]="_parenthesis_r"
    symbolnames["{"]="_bracket_l"
    symbolnames["}"]="_bracket_r"
    symbolnames["["]="_squarebracket_l"
    symbolnames["]"]="_squarebracket_r"

    symbolnames["<"]="_lessthan"
    symbolnames[">"]="_greaterthan"
    symbolnames["*"]="_asterisk"
    symbolnames["^"]="_caret"
    symbolnames["ˇ"]="_caron"
    symbolnames["°"]="_degree"
    symbolnames["+"]="_plus"
    symbolnames["="]="_equal"
    symbolnames["&"]="_ampersand"
    symbolnames["|"]="_vertical"
    symbolnames["%"]="_percentage"
    symbolnames["~"]="_tilde"
    symbolnames["¨"]="_umlaut"
    symbolnames["@"]="_at"
    symbolnames["$"]="_dollar"
    symbolnames["€"]="_euro"
    symbolnames["#"]="_hashtag"
    symbolnames["×"]="_multiplication"

add_symbols()


def symbols_to_txt():
    with open("symbolnames.txt","w") as fo:
        for symbol,name in sorted(symbolnames.items(), key=lambda item: item[1]):
            fo.write(symbol)
            fo.write(" ")
            fo.write(name)
            fo.write("\n")
    with open("symbols.txt","w") as fo:
        for symbol in sorted(symbolnames.keys()):
            fo.write(symbol)

def save_font():
    for symbol in symbolnames:
        disp_and_save(draw_symbol, symbol,filename_svg="gf_bg_"+symbolnames[symbol], display=False, res=256,bg=(1,1,1,1))
        disp_and_save(draw_symbol, symbol, filename_svg="gf_nobg_"+symbolnames[symbol], display=False, res=256)

def substitute_string(old_st):
    allowed=set(symbolnames.keys())
    old_st=old_st.lower()
    st=[]
    for char in old_st:
        match char:
            case "á":
                st.append("a´")
            case "é":
                st.append("e´")
            case "í":
                st.append("i´")
            case "ó":
                st.append("o´")
            case "ú":
                st.append("u´")
                
            case "à":
                st.append("a`")
            case "è":
                st.append("e`")
            case "ì":
                st.append("i`")
            case "ò":
                st.append("o`")
            case "ù":
                st.append("u`")
            case "â":
                st.append("a^")
            case "ê":
                st.append("e^")
            case "î":
                st.append("i^")
            case "ô":
                st.append("o^")
            case "û":
                st.append("u^")
            
            case "å":
                st.append("a°")
            # WEIRD BUG, skip for now
            # I assume that e̊ is broken into two characters, so they do not match the case
            #case "e̊":
            #    st.append("e°")
            #case "i̊":
            #    st.append("i°")
            case "o̊":
                st.append("o°")
            case "ů":
                st.append("u°")
            
            case "ä":
                st.append("a¨")
            case "ë":
                st.append("e¨")
            case "ï":
                st.append("i¨")
            case "ö":
                st.append("o¨")
            case "ü":
                st.append("u¨")
            case "ÿ":
                st.append("y¨")
            
            case default:
                if char in allowed:
                    st.append(char)
                else:
                    print(char, "Char not found")

    return "".join(st)

def draw_symbol_to_grid(cr: cairo.Context, symbol, line_width=0.01, rgb=(0,0,0), bg=(0,0,0,0)):
    
    cr.set_source_rgba(bg[0],bg[1],bg[2],bg[3])
    cr.rectangle(0,0,1,1)
    cr.fill()
    
    cr.set_line_width(line_width)
    cr.set_source_rgb(rgb[0], rgb[1], rgb[2])
    stroke_symbol(cr, symbol, line_width)
    
def to_grid(st:str,symbols_per_row=0):
    st=substitute_string(st)
    print(st)
    if symbols_per_row==0:
        symbols_per_row=math.ceil(math.sqrt(len(st)))
    rows=math.ceil(len(st)/symbols_per_row)
    print(len(st),symbols_per_row,rows)
    st=st+" "*(symbols_per_row*rows-len(st))

    
    CELL_SIZE=64
    WIDTH=CELL_SIZE*symbols_per_row
    HEIGHT=CELL_SIZE*rows
    # Create the output SVG surface
    with cairo.SVGSurface("attempt.svg", WIDTH, HEIGHT) as surface:
        cr = cairo.Context(surface)
        cr.set_line_width(0.01*WIDTH)
        for row in range(rows):
            for col in range(symbols_per_row):
                cr.save()
                cr.translate(col*CELL_SIZE,row*CELL_SIZE)
                cr.scale(CELL_SIZE,CELL_SIZE)
                draw_symbol_to_grid(cr,st[row*symbols_per_row+col],line_width=0.1,bg=(1,1,1,1))
                cr.restore()

symbols_to_txt()
save_font()

test_string="0123456789´`&'*@\\{}^:,-$=€¡!>#<()%.+¿?\";/ []~¨_|abcdefghijklmnopqrstuvwxyzñáèôåe̊E̊i̊ůŮ°ˇ"
#to_grid(test_string)
to_grid("abf  ")


