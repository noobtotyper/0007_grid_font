import math

import cairo
from io import BytesIO
import random
from SymbolDrawerSmooth import SymbolDrawerSmooth
from Connections import get_flows



def disp_and_save(
    draw_func,
    symbol,
    display=False,
    folder="Icons/",
    filename_png=None,
    filename_svg=None,
    res=256,
    line_width=0.1,
):
    width = res
    height = res

    # Create an ImageSurface for PNG display
    surface_png = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx_png = cairo.Context(surface_png)
    ctx_png.scale(width,height)
    draw_func(ctx_png, symbol, line_width=line_width)
    
    if filename_png:
        surface_png.write_to_png(folder + "PNG/" + filename_png + ".png")

    if filename_svg:
        # Create an SVGSurface to save the image as SVG
        surface_svg = cairo.SVGSurface(
            folder + "SVG/" + filename_svg + ".svg", width, height
        )
        ctx_svg = cairo.Context(surface_svg)
        ctx_svg.scale(width,height)
        draw_func(ctx_svg, symbol, line_width=line_width)
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



def get_symbolsnames():
    symbolnames = {
    symbol: "_" + symbol for symbol in "abcdefghijklmnñopqrstuvwxyz0123456789"
}
    symbolnames[" "] = "space"
    symbolnames["-"] = "dash"
    symbolnames["_"] = "underscore"
    symbolnames["."] = "period"
    symbolnames[","] = "comma"
    symbolnames[":"] = "colon"
    symbolnames[";"] = "semicolon"
    symbolnames["¿"] = "question_l"
    symbolnames["?"] = "question_r"
    symbolnames["¡"] = "exclamation_l"
    symbolnames["!"] = "exclamation_r"
    symbolnames["'"] = "apostrophe"
    symbolnames['"'] = "quotation"
    symbolnames["´"] = "accent_acute"
    symbolnames["`"] = "accent_grave"
    symbolnames["/"] = "slash"
    symbolnames["\\"] = "backslash"
    symbolnames["("] = "parenthesis_l"
    symbolnames[")"] = "parenthesis_r"
    symbolnames["{"] = "bracket_l"
    symbolnames["}"] = "bracket_r"
    symbolnames["["] = "squarebracket_l"
    symbolnames["]"] = "squarebracket_r"
    symbolnames["<"] = "lessthan"
    symbolnames[">"] = "greaterthan"
    symbolnames["*"] = "asterisk"
    symbolnames["^"] = "caret"
    symbolnames["ˇ"] = "caron"
    symbolnames["°"] = "degree"
    symbolnames["+"] = "plus"
    symbolnames["="] = "equal"
    symbolnames["&"] = "ampersand"
    symbolnames["|"] = "vertical"
    symbolnames["%"] = "percentage"
    symbolnames["~"] = "tilde"
    symbolnames["¨"] = "umlaut"
    symbolnames["@"] = "at"
    symbolnames["$"] = "dollar"
    symbolnames["€"] = "euro"
    symbolnames["#"] = "hashtag"
    symbolnames["×"] = "multiplication"
    symbolnames["⭾"] = "tab"
    symbolnames["⏎"] = "return"
    symbolnames["¤"] = "currency"
    symbolnames["ß"] = "eszett"
    symbolnames["¬"] = "not"
    symbolnames["¸"] = "cedilla"
    symbolnames["ç"] = "cedilla_c"
    symbolnames["«"] = "double_angle_l"
    symbolnames["»"] = "double_angle_r"
    symbolnames["£"] = "pound"
    symbolnames["·"] = "dot"
    symbolnames["–"] = "en_dash"
    symbolnames["—"] = "em_dash"
    symbolnames["−"] = "minus"
#    symbolnames[""] = ""
    return symbolnames

def symbols_to_txt(symbolsnames):
    with open("symbolnames.txt", "w") as fo:
        for symbol, name in sorted(symbolsnames.items(), key=lambda item: item[1]):
            fo.write(symbol)
            fo.write(" ")
            fo.write(name)
            fo.write("\n")
    with open("symbols.txt", "w") as fo:
        for symbol, _ in sorted(symbolsnames.items(), key=lambda item: item[1]):
            fo.write(symbol)


def save_font(symbolsnames,filename_prefix="gf_example_",png=False,svg=True, display=False,res=256,stroke_semiwidth=1/20,corners=True, rgb=(0, 0, 0), bg=(1,1,1,1)):
    symbolsmooth = SymbolDrawerSmooth(stroke_semiwidth=stroke_semiwidth,corners=corners, rgb=rgb, bg=bg)
    if png:
        filenames_png={symbol:filename_prefix+symbolsnames[symbol] for symbol in symbolsnames}
    else:
        filenames_png={}
    if svg:
        filenames_svg={symbol:filename_prefix+symbolsnames[symbol] for symbol in symbolsnames}
    else:
        filenames_svg={}
        
    for symbol in symbolsnames:
        disp_and_save(
            symbolsmooth.draw_symbol,
            symbol,
            filename_png=filenames_png.get(symbol,None),
            filename_svg=filenames_svg.get(symbol,None),
            display=display,
            res=res,
        )




def substitute_string(symbolsnames,old_st,spaces_newline=1,spaces_tab=1):
    assert type(spaces_newline)==int
    assert type(spaces_tab)==int
        
    allowed = set(symbolsnames.keys())
    old_st = old_st.lower()
    st = []
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
            # case "e̊":
            #    st.append("e°")
            # case "i̊":
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

            case "’":
                st.append("'")
            case "\t":
                st.append("⭾"+" "*spaces_newline)
            case "\n":
                st.append("⏎"+" "*spaces_newline)
            
            case default:
                if char in allowed:
                    st.append(char)
                else:
                    print(char, "Char not found")

            
    return "".join(st)

def substitute_string_line_by_line(symbolsnames,text,spaces_tab=1, symbols_per_row=0,returnchar=False, debug=False):
    lines=[substitute_string(symbolsnames,line).rstrip() for line in text.split("\n")]
    if not symbols_per_row:
        symbols_per_row=max([len(line) for line in lines])
        if returnchar:
            symbols_per_row+=1
    out_lines=[]
    for line in lines:
        # the bug might originate here
        aux=len(line)%(symbols_per_row)
        if aux!=0 or len(line)==0:
            padding=symbols_per_row-len(line)%symbols_per_row
        else:
            padding=0
        if returnchar:
            # there is a bug here if padding is 0
            # maybe it will only happen if a line that is not the longest ends where the returns go
            out_lines.append(line+" "*(padding-1)+"⏎")
        else:
            out_lines.append(line+" "*padding)

    if debug:
        for line in out_lines:
            print(line.replace(" ","_"))
            
    out_text="".join(out_lines)
    return out_text, symbols_per_row

def to_grid(symbolsnames,st: str, filename="output_grid",line_by_line=False,returnchar=False,symbols_per_row=0,stroke_semiwidth=math.sqrt(5)/20, corners= True, rgb=(0, 0, 0), rgb_end=None, bg=(1, 1, 1, 1), bg_end=None, debug=True):
    if line_by_line:
        st,symbols_per_row=substitute_string_line_by_line(symbolsnames=symbolsnames,text=st,symbols_per_row=symbols_per_row,returnchar=returnchar,debug=debug)
    else:
        st = substitute_string(symbolsnames,st)
        if symbols_per_row == 0:
            symbols_per_row = math.ceil(math.sqrt(len(st)))
        if debug:
            print(st)
    
        
    rows = math.ceil(len(st) / symbols_per_row)
    print(len(st), symbols_per_row, rows)
    st = st + " " * (symbols_per_row * rows - len(st))

    CELL_SIZE = 64
    WIDTH = CELL_SIZE * symbols_per_row
    HEIGHT = CELL_SIZE * rows
    # Create the output SVG surface
    with cairo.SVGSurface(filename+".svg", WIDTH, HEIGHT) as surface:
        cr = cairo.Context(surface)
        symbol_smooth_drawer = SymbolDrawerSmooth(stroke_semiwidth=stroke_semiwidth,corners=corners, rgb=rgb, bg=bg)
        if rgb_end:
            min_rgb_r=min(rgb[0],rgb_end[0])
            max_rgb_r=max(rgb[0],rgb_end[0])
            dif_rgb_r=max_rgb_r-min_rgb_r
            min_rgb_g=min(rgb[1],rgb_end[1])
            max_rgb_g=max(rgb[1],rgb_end[1])
            dif_rgb_g=max_rgb_g-min_rgb_g
            min_rgb_b=min(rgb[2],rgb_end[2])
            max_rgb_b=max(rgb[2],rgb_end[2])
            dif_rgb_b=max_rgb_b-min_rgb_b
        if bg_end:
            min_bg_r=min(bg[0],bg_end[0])
            max_bg_r=max(bg[0],bg_end[0])
            dif_bg_r=max_bg_r-min_bg_r
            min_bg_g=min(bg[1],bg_end[1])
            max_bg_g=max(bg[1],bg_end[1])
            dif_bg_g=max_bg_g-min_bg_g
            min_bg_b=min(bg[2],bg_end[2])
            max_bg_b=max(bg[2],bg_end[2])
            dif_bg_b=max_bg_b-min_bg_b
            min_bg_a=min(bg[3],bg_end[3])
            max_bg_a=max(bg[3],bg_end[3])
            dif_bg_a=max_bg_a-min_bg_a
        for row in range(rows):
            for col in range(symbols_per_row):                
                if rgb_end:
                    r=dif_rgb_r*row/rows+min_rgb_r
                    g=dif_rgb_g*(row+col)/(rows+symbols_per_row)+min_rgb_g
                    b=dif_rgb_b*col/symbols_per_row+min_rgb_b
                    symbol_smooth_drawer.change_rgb((r,g,b))
                if bg_end:
                    r=dif_bg_r*(1-row/rows)+min_bg_r
                    g=dif_bg_g*(1-(row+col)/(rows+symbols_per_row))+min_bg_g
                    b=dif_bg_b*(1-col/symbols_per_row)+min_bg_b
                    a=dif_bg_a *(1-(row*col)/(rows*symbols_per_row))+min_bg_a
                    symbol_smooth_drawer.change_bg((r,g,b,a))
                cr.save()
                cr.translate(col * CELL_SIZE, row * CELL_SIZE)
                cr.scale(CELL_SIZE, CELL_SIZE)
                symbol_smooth_drawer.draw_symbol(cr, st[row * symbols_per_row + col])
                cr.restore()

def fonts(symbolsnames,alphabet_string):
    """This function does the same for each of the 4 configurations of parameters.
    It saves the alphabet in a 11 by 9 grid, and also symbol by symbol."""
    thick=1/10
    medium=1/20

    save_font(symbolsnames, filename_prefix="gf_cor_medium_",stroke_semiwidth=medium,corners=True)
    save_font(symbolsnames,filename_prefix="gf_cor_thick_",stroke_semiwidth=thick,corners=True)
    save_font(symbolsnames, filename_prefix="gf_nocor_medium_",stroke_semiwidth=medium,corners=False)
    save_font(symbolsnames,filename_prefix="gf_nocor_thick_",stroke_semiwidth=thick,corners=False)
    print(alphabet_string)
    to_grid(symbolsnames,alphabet_string,filename="GridFontAlphabetCorMedium",symbols_per_row=9,stroke_semiwidth=medium,corners=True)
    to_grid(symbolsnames,alphabet_string,filename="GridFontAlphabetCorThick",symbols_per_row=9,stroke_semiwidth=thick,corners=True)
    to_grid(symbolsnames,alphabet_string,filename="GridFontAlphabetNoCorMedium",symbols_per_row=9,stroke_semiwidth=medium,corners=False)
    to_grid(symbolsnames,alphabet_string,filename="GridFontAlphabetNoCorThick",symbols_per_row=9,stroke_semiwidth=thick,corners=False)

def runningoutofink(symbolsnames):
    rooi="""I am running out of ink
My thoughts keep shuffling
Looking for a pen to make history
I don’t have much of a declarative mind
So I certainly need a pen
To put my scattered thoughts together

Every thought inscribed and shared
Is an opportunity to spread
Fundamental experiences

The gold the silver the diamonds
The paintings and antiques
Mean nothing to me if it’s just the rich ones
That can get their hands into it

Dear brain of mine
Please save these thoughts of mine
Invest my thinking for future use """
    to_grid(symbolsnames,st=rooi,symbols_per_row=0,returnchar=True,line_by_line=True,filename="RunningOutOfInk",corners=False)

def heysis(symbolsnames):
    heysis="""Hey sis,

I hope my letters have been reaching you and Dad. Hand-written stuff's never been super reliable, but I guess it's all we've got these days. Anyway, in case you haven't been getting them, I want to say I'm sorry for leaving the way I did. I know you told me it was a reckless idea, and after everything I've been through, I can definitely say you were right. It's been hard on all of us. And I'm not just talking about the monsters we fought out here.

Every step we made took us further and further away from the things we knew, and every morning we woke up wondering if just over the next hill would be something good or something terrible. It's scary... not knowing what's going to happen next, and the things we do know now; just how bad it can get... almost makes it all worse. You told me once that bad things just happen. You were angry when you said it and I didn’t want to listen. But you were right. Bad things do happen. All the time every day. Which is why I’m out here to do whatever I can, wherever I can. And hopefully do some good. We’ve all lost something, and I’ve seen what loss can do to people. But if we gave up every time we lost, then we’d never be able to move forward. We'd never have a chance to see what beautiful things the future might have waiting for us. We'd never have the strength to change. Whether it's ourselves, or the world around us. And we'd never be there for other people who might one day be lost without us.

This is what we were training for, Yang. To become Huntresses. To be the ones to stand up and do something about all the bad in the world. Because there are plenty of people out there who are still lost, and even more who will try to gain everything they can from their sorrow. Believe me when I say I know it can feel impossible. Like every single day is a struggle against some unstoppable monster we can never hope to beat. So we have to try. If not for us, then for the ~people we've already~ people we haven't lost yet. I miss you so much. I miss Weiss and Blake too. But I think you'd all be proud to know that I made it to Mistral. All of us did. We even ran into Uncle Qrow along the way! He's going to take us to see Professor Lionheart, the Headmaster at Haven Academy. And, he told us some things that you're gonna wanna hear, things I can't trust will make it to you in this letter. But maybe, if you joined us, he could tell you himself. With Beacon gone, they'll need Dad at Signal more than ever. And I know you need to focus on yourself before I can expect you to come out with me, but it sure would be great to get Team RWBY back together again.

Until next time, your loving sister,
~Ruby Rose 🌹


Oh! Uh! PS: I'll be sure to give you the adress of where we'll be staying at Mistral. I'd love to hear from you and dad, and I can't wait to fill you in whatever's going to happen next! Now that we've made it across Anima, I really think things are gonna start going our way."""
    to_grid(symbolsnames,st=heysis,symbols_per_row=0,returnchar=True,line_by_line=False,filename="HeySis",corners=False)

def random_grid(symbolsnames,alphabet_string,k=900):
    to_grid(symbolsnames,"".join(random.choices(alphabet_string,k=k)),stroke_semiwidth=math.sqrt(5)/20,filename="random",corners=False)

def random_flow_string(symbolsnames:dict,rows,cols, flowtype=1,debug=False):
    assert type(rows)==int and rows>0
    assert type(cols)==int and cols>0
    assert flowtype==1 or flowtype==3
    h3flows, v3flows, h1flows, v1flows, connections= get_flows(symbolsnames)
    cells=[]
    
    cells.append(random.choice([symbol for symbol in symbolsnames]))
    if flowtype==1:
        for i in range(1,cols):
            connects=connections[cells[i-1]][5] # select the index, 0 does not connect, 1 does
            cells.append(random.choice(h1flows[connects][1])) # pick from the set for right cells
        for row in range(1, rows):
            # leftmost elements
            connects=connections[cells[(row-1)*cols]][7]
            cells.append(random.choice(v1flows[connects][1])) # pick from bottom set
            for col in range(1,cols):
                hconnects=connections[cells[row*cols+col-1]][5]
                vconnects=connections[cells[(row-1)*cols+col]][7]
                cells.append(random.choice(h1flows[hconnects][1]&v1flows[vconnects][1])) # this is why I use Indexed set, I will need both operations
    else:
        raise Exception("Not implemented yet")
    
    if debug:
        print("Generated string")
        for row in range(rows):
            for col in range(cols):
                if row*cols+col<len(cells):
                    print(cells[row*cols+col],end=" ")
            print()
        print()
    
    return "".join(cells)

def random_flowing_words(nof_words=50):
    with open("FlowingWords.txt", "r") as f:
        valid_words=[line.strip() for line in f.readlines()]
    return " ".join(random.choices(valid_words,k=nof_words))

def main():
    
    symbolsnames=get_symbolsnames()
    symbols_to_txt(symbolsnames)
    
    alphabet_string = ("".join([symbol for symbol in symbolsnames]))
    fonts(symbolsnames,alphabet_string)

    #to_grid(symbolsnames,"Nothing lasts forever",filename="NothingLastsForever",stroke_semiwidth=1/20,symbols_per_row=7,corners=False)
    #runningoutofink(symbolsnames)
    #heysis(symbolsnames)
    #random_grid(symbolsnames,alphabet_string)
    
    rfs=random_flow_string(symbolsnames,30,30, debug=True)
    #to_grid(symbolsnames,rfs,stroke_semiwidth=math.sqrt(5)/20,filename="RandomFlow",rgb=(0,0,0),rgb_end=(1,1,1),bg=(1,1,1,1),bg_end=(0,0,0,1),corners=False)
    to_grid(symbolsnames,rfs,stroke_semiwidth=math.sqrt(5)/20,filename="RandomFlow",rgb=(1,1,1),bg=(0,0,0,1),corners=True)

    #to_grid(symbolsnames, random_flowing_words(50),stroke_semiwidth=math.sqrt(5)/20,filename="RandomFlowWords",rgb=(0,0,0),bg=(1,1,1,1),corners=False)

main()
