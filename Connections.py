from itertools import product
from boltons.setutils import IndexedSet

def read_connections(meaning={'tl':0,'t':1,'tr':2,'l':3,'c':4,'r':5,'bl':6,'b':7,'br':8}):
    connections={}

    with open("SymbolDrawerBlocky.py","r") as f:
        lines = f.readlines()
        
        first=0
        while "fill_symbol" not in lines[first]:
            first+=1
        last=len(lines)-1
        while "def draw_symbol(" not in lines[last]:
            last-=1
        #valid=set(['tl','t','tr','l','c','r','bl','b','br'])
        valid=set(['tl','t','tr','l','r','bl','b','br'])
        
        current=""
        for i,line in enumerate(lines[first+1:last]):
            st=line.strip()
            if "case" in st:
                if not "default" in st:
                    current=st[6]
                    connections[current]=[0,0,0,0,0,0,0,0,0]
            elif st[:5]=="self.":
                par=st.find("(")
                positions=st[5:par].split("_")
                for pos in positions:
                    if pos in valid:
                        connections[current][meaning[pos]]=1
    
    connections["—"][5]=1
    #connections["−"][5]=1
    return connections

def print_connections(symbolsnames,connections):
    print(''.join([symbol for symbol in symbolsnames]))

    for symbol in symbolsnames:
        print(symbol, end=" ")
        for con in connections[symbol]:
            print(con, end="")
        print()

def match_l_r(l,r,size=3):
    """Checks whether l to r is a valid connection\n
    Returns True if all the connections on the right side of l match all the connections on the left side of r\n
    Returns False otherwise\n
    
    (no type checking, assuming tuple or list of length >= 9)"""
    
    last=size-1
    for idx in range(size):
        if l[idx*size+last]!=r[idx*size]:
            return False
    return True

def match_t_b(t,b,size=3):
    """Checks whether t to b is a valid connection\n
    Returns True if all the connections on the bottom side of t match all the connections on the top side of b\n
    Returns False otherwise\n
    
    (no type checking, assuming tuple or list of length >= 9)"""
    last=size*size-size
    for idx in range(size):
        if t[idx+last]!=b[idx]:
            return False
    return True

def get_threeflows(symbolsnames, connections):
    possible_junctions=list(product((0,1), (0,1), (0,1)))
    
    # in hflows the tuple is top to bottom (entry per each row)
    # the values are (leftset, rightset)
    hflows={tup:(IndexedSet(),IndexedSet()) for tup in possible_junctions}
    
    # in vflows the tuple is left to rigth (entry per each col)
    # the values are (topset, bottomset)
    vflows={tup:(IndexedSet(),IndexedSet()) for tup in possible_junctions}

    for l_symbol in symbolsnames:
        for r_symbol in symbolsnames:
            connect=match_l_r(connections[l_symbol],connections[r_symbol])
            if connect:
                r=connections[r_symbol]
                tup=(r[0],r[3],r[6])
                hflows[tup][0].add(l_symbol)
                hflows[tup][1].add(r_symbol)
                
    for t_symbol in symbolsnames:
        for b_symbol in symbolsnames:
            connect=match_t_b(connections[t_symbol],connections[b_symbol])
            if connect:
                b=connections[b_symbol]
                tup=(b[0],b[1],b[2])
                vflows[tup][0].add(t_symbol)
                vflows[tup][1].add(b_symbol)
    
    return hflows, vflows

def get_oneflows(symbolsnames, connections):
    
    # in hflows index 0 means no line, 1 means line
    # the values are (leftset, rightset)
    hflows=[(IndexedSet(),IndexedSet()) for _ in range(2)]
    
    # in vflows 0 means no line, 1 means line
    # the values are (topset, bottomset)
    vflows=[(IndexedSet(),IndexedSet()) for _ in range(2)]

    for l_symbol in symbolsnames:
        for r_symbol in symbolsnames:
            if connections[l_symbol][5]==connections[r_symbol][3]:
                idx=connections[r_symbol][3]
                hflows[idx][0].add(l_symbol)
                hflows[idx][1].add(r_symbol)
                
    for t_symbol in symbolsnames:
        for b_symbol in symbolsnames:
            if connections[t_symbol][7]==connections[b_symbol][1]:
                idx=connections[b_symbol][1]
                vflows[idx][0].add(t_symbol)
                vflows[idx][1].add(b_symbol)
    
    return hflows, vflows


def print_flows(flows):
    if type(flows)==list:
        for flow in flows:
            print(flow)
            print()
        print()
    else:
        for flow in flows:
            print(flow)
            print(flows[flow][0])
            print(flows[flow][1])
            print()

def print_both_flows(hflows, vflows):
    print("hflows")
    print_flows(hflows)
    print()
    print("vflows")
    print_flows(vflows)


def get_flows(symbolsnames):
    connections=read_connections()

    #print_connections(symbolsnames,connections)

    h3flows, v3flows = get_threeflows(symbolsnames,connections)
    h1flows, v1flows = get_oneflows(symbolsnames,connections)
    
    #print_connections(symbolsnames, connections)
    print_both_flows(h3flows,v3flows)
    #print_both_flows(h1flows, v1flows)
    return h3flows, v3flows, h1flows, v1flows, connections

#symbolsnames=get_symbolsnames()
    