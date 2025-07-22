import cairo

SQUARE_SIZE = 100
WIDTH = HEIGHT = SQUARE_SIZE * 2

def draw_square1(ctx):
    ctx.set_source_rgb(1, 0, 0)  # Red
    ctx.rectangle(0, 0, 1, 1)
    ctx.fill()

def draw_square2(ctx):
    ctx.set_source_rgb(0, 1, 0)  # Green
    ctx.rectangle(0, 0, 1, 1)
    ctx.fill()

def draw_square3(ctx):
    ctx.set_source_rgb(0, 0, 1)  # Blue
    ctx.rectangle(0, 0, 1, 1)
    ctx.fill()

def draw_square4(ctx):
    ctx.set_source_rgb(1, 1, 0)  # Yellow
    ctx.rectangle(0, 0, 1, 1)
    ctx.fill()

# Create the output SVG surface
with cairo.SVGSurface("combined.svg", WIDTH, HEIGHT) as surface:
    ctx = cairo.Context(surface)
    
    
    # Top-left
    ctx.save()
    ctx.translate(0, 0)
    ctx.scale(SQUARE_SIZE,SQUARE_SIZE)
    draw_square1(ctx)
    ctx.restore()

    # Top-right
    ctx.save()
    ctx.translate(SQUARE_SIZE, 0)
    ctx.scale(SQUARE_SIZE,SQUARE_SIZE)
    draw_square2(ctx)
    ctx.restore()

    # Bottom-left
    ctx.save()
    ctx.translate(0, SQUARE_SIZE)
    ctx.scale(SQUARE_SIZE,SQUARE_SIZE)
    draw_square3(ctx)
    ctx.restore()

    # Bottom-right
    ctx.save()
    ctx.translate(SQUARE_SIZE, SQUARE_SIZE)
    ctx.scale(SQUARE_SIZE,SQUARE_SIZE)
    draw_square4(ctx)
    ctx.restore()