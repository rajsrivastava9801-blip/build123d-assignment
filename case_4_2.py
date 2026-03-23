import math
from build123d import *
from ocp_vscode import show_all, set_port

set_port(3939)

LENGTH         = 105.8
WIDTH          =  81.3
TOTAL_HEIGHT   =  13.0
SHEET_T        =   1.0
WALL_T         =   1.0
HOLE_DIA       =   4.19249
HOLE_OFFSET    =   4.5
OVERCUT        =   0.1
SQUARE_SIZE    =   7.0
SQUARE_GAP     =   5.0
FIRST_OFFSET   =  32.56609
SQ_TOP_OFFSET  =   3.0
PIN_DIA        =   2.0
PIN_HEIGHT     =   8.0
PIN1_FROM_FRONT =  16.85180
PIN1_FROM_RIGHT =   4.05619
PIN2_FROM_BACK  =  15.56520
PIN2_FROM_RIGHT =   4.354484
PIN3_FROM_FRONT =  16.73047
PIN3_FROM_RIGHT =  45.55975
PIN4_FROM_BACK  =  24.11585
PIN4_FROM_RIGHT =  46.91619
SLOT1_L        =  30.25600
SLOT1_W        =  18.80000
SLOT1_FROM_FRONT =  25.12800
SLOT1_FROM_RIGHT =  30.60000
SLOT2_L        =  23.71100
SLOT2_W        =   5.84100
SLOT2_FROM_FRONT =  40.63195
SLOT2_FROM_RIGHT =   3.92050
SLOT3_L        =  22.20000
SLOT3_W        =  13.06700
SLOT3_FROM_LEFT  =   7.03010
SLOT3_FROM_FRONT =  40.80000
SLOT4_L        =   9.15500
SLOT4_W        =  17.58100
SLOT4_FROM_FRONT =  32.01650
SLOT4_FROM_RIGHT =  51.46550
WEDGE_BASE_L   =  15.0
WEDGE_BASE_W   =   8.0
WEDGE_HEIGHT   =   8.0
WEDGE_FROM_INNER = 15.0
RING_OUTER_L   =  33.50
RING_OUTER_W   =  56.00
RING_INNER_L   =  31.50
RING_INNER_W   =  48.00
RING_HEIGHT    =  10.85
RING_FROM_RIGHT =  79.40
RING_FROM_FRONT =  40.65
RING_BASE_T    =   1.5
RING_BASE_INSET =   0.15
RING_HOLE_L    =   6.6   # fallback (unused after per-hole below)
# Per-hole widths (left-to-right span of each rectangular cut)
H1_L = 6.2   # front right   (normal)
H2_L = 6.6   # front middle  (slant)
H3_L = 6.2   # front left    (normal)
H4_L = 6.6   # back  right   (slant)
H5_L = 6.2   # back  middle  (normal)
H6_L = 6.6   # back  left    (slant)
RING_HOLE_W    =   2.50
RING_HOLE_D    =   9.00
RING_HOLE_FROM_EDGE = 3.15
RING_HOLE2_W   =   1.50
RING_HOLE2_D   =   2.00
RING_BACK_HOLE_FROM_EDGE = 13.65
SQ_HOLE_SIZE   =   1.30
SQ_HOLE_DEPTH  =   1.00
SQ_HOLE_FROM_BASE  =   3.20
RING_HOLE3_D   =   7.50
RING_HOLE3_FROM_RIGHT = 13.45
SLANT_ANGLE_DEG    =  16.73
SLANT_H            =   1.91086
SLANT_DEPTH        =  SLANT_H * math.cos(math.radians(SLANT_ANGLE_DEG))
SLANT_X_TAPER      =  SLANT_H * math.sin(math.radians(SLANT_ANGLE_DEG))
BOTTOM_CUT_W       =   4.0
BOTTOM_CUT_D_Z     =   1.0

# ─── Scoop dims ───────────────────────────────────────────────
SCOOP_SAG      =  1.4503          # sagitta downward from RING_BASE_TOP_Z
SCOOP_W        =  RING_INNER_L / 3  # 10.5mm each

# ─── Rectangular solid (rib flush with base top) ──────────────
RIB_W          =  2.0     # X: right to left
RIB_H          =  0.5     # Z: top to bottom
RIB_FROM_INNER =  9.5     # right face of rib from RING_INNER_RIGHT_X

# ─── Through-all rectangular cut ─────────────────────────────
TCUT_L           =  10.755
TCUT_W           =  17.005
TCUT_FROM_FRONT  =  35.44150
TCUT_FROM_RIGHT  =  71.65050

# ─── Rectangular slab dims ────────────────────────────────────
SLAB_WIDTH     =  2.0             # X dimension
SLAB_DEPTH     =  0.502           # Z dimension (top to bottom)
SLAB_FROM_R    =  9.5             # right edge of slab 1 from RING_RIGHT_EDGE_X
SLAB_FROM_L    =  9.5             # left  edge of slab 2 from RING_LEFT_EDGE_X
SLAB_FROM_TOP  =  9.5             # kept for reference — 3 equal chords

WALL_HEIGHT    = TOTAL_HEIGHT - SHEET_T
CAVITY_L       = LENGTH - 2 * WALL_T
CAVITY_W       = WIDTH  - 2 * WALL_T

X_R =  LENGTH / 2 - HOLE_OFFSET
X_L = -LENGTH / 2 + HOLE_OFFSET
Y_T =  WIDTH  / 2 - HOLE_OFFSET
Y_B = -WIDTH  / 2 + HOLE_OFFSET

SQ_X1 =  LENGTH / 2 - FIRST_OFFSET - SQUARE_SIZE / 2
SQ_X2 =  SQ_X1 - (SQUARE_SIZE + SQUARE_GAP)
SQ_X3 =  SQ_X2 - (SQUARE_SIZE + SQUARE_GAP)
SQ_X4 =  SQ_X3 - (SQUARE_SIZE + SQUARE_GAP)
SQ_SK_Y = SQ_TOP_OFFSET + SQUARE_SIZE / 2

PIN1_X =  LENGTH / 2 - PIN1_FROM_RIGHT
PIN1_Y = -WIDTH  / 2 + PIN1_FROM_FRONT
PIN2_X =  LENGTH / 2 - PIN2_FROM_RIGHT
PIN2_Y =  WIDTH  / 2 - PIN2_FROM_BACK
PIN3_X =  LENGTH / 2 - PIN3_FROM_RIGHT
PIN3_Y = -WIDTH  / 2 + PIN3_FROM_FRONT
PIN4_X =  LENGTH / 2 - PIN4_FROM_RIGHT
PIN4_Y =  WIDTH  / 2 - PIN4_FROM_BACK

SLOT1_X =  LENGTH / 2 - SLOT1_FROM_RIGHT
SLOT1_Y = -WIDTH  / 2 + SLOT1_FROM_FRONT
SLOT2_X =  LENGTH / 2 - SLOT2_FROM_RIGHT
SLOT2_Y = -WIDTH  / 2 + SLOT2_FROM_FRONT
SLOT3_X = -LENGTH / 2 + SLOT3_FROM_LEFT
SLOT3_Y = -WIDTH  / 2 + SLOT3_FROM_FRONT
SLOT4_X =  LENGTH / 2 - SLOT4_FROM_RIGHT
SLOT4_Y = -WIDTH  / 2 + SLOT4_FROM_FRONT

RING_X  =  LENGTH / 2 - RING_FROM_RIGHT
RING_Y  = -WIDTH  / 2 + RING_FROM_FRONT
RING_BASE_Z     = SHEET_T - RING_BASE_INSET
RING_BASE_TOP_Z = RING_BASE_Z + RING_BASE_T

RING_RIGHT_EDGE_X  =  RING_X + RING_OUTER_L / 2
RING_LEFT_EDGE_X   =  RING_X - RING_OUTER_L / 2
RING_INNER_RIGHT_X =  RING_X + RING_INNER_L / 2
RING_INNER_LEFT_X  =  RING_X - RING_INNER_L / 2
# Per-hole center X (FROM_EDGE is outer-edge → near-edge of hole)
H1_CX = RING_RIGHT_EDGE_X - RING_HOLE_FROM_EDGE - H1_L / 2   # front right
H2_CX = RING_RIGHT_EDGE_X - RING_HOLE3_FROM_RIGHT - H2_L / 2 # front middle (slant)
H3_CX = RING_LEFT_EDGE_X  + RING_HOLE_FROM_EDGE + H3_L / 2   # front left
H4_CX = RING_RIGHT_EDGE_X - RING_HOLE_FROM_EDGE - H4_L / 2   # back  right (slant)
H5_CX = RING_X                                                 # back  middle (centred)
H6_CX = RING_LEFT_EDGE_X  + RING_HOLE_FROM_EDGE + H6_L / 2   # back  left (slant)
# Keep legacy names as aliases for any unchanged references
RING_HOLE_R_X = H1_CX
RING_HOLE_L_X = H3_CX
RING_HOLE3_X  = H2_CX

RING_FRONT_Y       =  RING_Y - RING_OUTER_W / 2
RING_HOLE_FY       =  RING_FRONT_Y + RING_HOLE_W / 2
RING_HOLE_BACK_FY  =  RING_FRONT_Y + RING_HOLE_W
RING_HOLE2_FY      =  RING_HOLE_BACK_FY + RING_HOLE2_W / 2
RING_BACK_Y        =  RING_Y + RING_OUTER_W / 2
RING_HOLE_BY       =  RING_BACK_Y - RING_HOLE_W / 2
RING_HOLE_BACK_BY  =  RING_BACK_Y - RING_HOLE_W
RING_HOLE2_BY      =  RING_HOLE_BACK_BY - RING_HOLE2_W / 2
RING_INNER_FRONT_Y =  RING_FRONT_Y + (RING_OUTER_W - RING_INNER_W) / 2
RING_INNER_BACK_Y  =  RING_BACK_Y  - (RING_OUTER_W - RING_INNER_W) / 2

RING_HOLE_Z_TOP    =  SHEET_T + RING_HEIGHT + OVERCUT
RING_HOLE_Z_BOT    =  SHEET_T + RING_HEIGHT - RING_HOLE_D
SQ_HOLE_Z_CTR      =  RING_HOLE_Z_BOT + SQ_HOLE_FROM_BASE + SQ_HOLE_SIZE / 2
RING_HOLE3_Z_BOT   =  RING_HOLE_Z_TOP - (RING_HOLE3_D + 2 * OVERCUT)
SLANT_Z_BOT        =  RING_HOLE3_Z_BOT - SLANT_DEPTH

RING_SQ_R_LEFT_X   =  H1_CX - H1_L / 2 + SQ_HOLE_SIZE / 2   # hole 1 front
RING_SQ_R_RIGHT_X  =  H1_CX + H1_L / 2 - SQ_HOLE_SIZE / 2
RING_SQ_L_LEFT_X   =  H3_CX - H3_L / 2 + SQ_HOLE_SIZE / 2   # hole 3 front
RING_SQ_L_RIGHT_X  =  H3_CX + H3_L / 2 - SQ_HOLE_SIZE / 2
RING_BACK_HOLE_X   =  RING_X
RING_SQ_B_LEFT_X   =  H5_CX - H5_L / 2 + SQ_HOLE_SIZE / 2   # hole 5 back
RING_SQ_B_RIGHT_X  =  H5_CX + H5_L / 2 - SQ_HOLE_SIZE / 2
RING_SQ3_LEFT_X    =  H2_CX - H2_L / 2 + SQ_HOLE_SIZE / 2   # hole 2 front (slant)
RING_SQ3_RIGHT_X   =  H2_CX + H2_L / 2 - SQ_HOLE_SIZE / 2
RING_SQ_BR_LEFT_X  =  H4_CX - H4_L / 2 + SQ_HOLE_SIZE / 2   # hole 4 back (slant)
RING_SQ_BR_RIGHT_X =  H4_CX + H4_L / 2 - SQ_HOLE_SIZE / 2
RING_SQ_BL_LEFT_X  =  H6_CX - H6_L / 2 + SQ_HOLE_SIZE / 2   # hole 6 back (slant)
RING_SQ_BL_RIGHT_X =  H6_CX + H6_L / 2 - SQ_HOLE_SIZE / 2

SQ_FRONT_Y_CTR  =  RING_FRONT_Y + RING_HOLE_W + SQ_HOLE_DEPTH / 2
SQ_BACK_Y_CTR   =  RING_BACK_Y  - RING_HOLE_W - SQ_HOLE_DEPTH / 2

slant_front_plane = Plane(origin=(0, RING_FRONT_Y - OVERCUT, 0), x_dir=(1,0,0), z_dir=(0,1,0))
slant_back_plane  = Plane(origin=(0, RING_BACK_Y  + OVERCUT, 0), x_dir=(1,0,0), z_dir=(0,-1,0))

INNER_RIGHT_X   =  LENGTH / 2 - WALL_T
R_WEDGE_X_LEFT  =  INNER_RIGHT_X - WEDGE_FROM_INNER - WEDGE_BASE_L
INNER_LEFT_X    = -LENGTH / 2 + WALL_T
INNER_FRONT_Y  = -WIDTH / 2 + WALL_T
INNER_BACK_Y   =  WIDTH / 2 - WALL_T
WEDGE_Z_START  =  TOTAL_HEIGHT - WEDGE_HEIGHT

wedge_rf_plane = Plane(origin=(R_WEDGE_X_LEFT, INNER_FRONT_Y, WEDGE_Z_START), x_dir=(0,1,0), z_dir=(1,0,0))
wedge_rb_plane = Plane(origin=(R_WEDGE_X_LEFT, INNER_BACK_Y,  WEDGE_Z_START), x_dir=(0,-1,0), z_dir=(1,0,0))
wedge_lf_plane = Plane(origin=(INNER_LEFT_X,   INNER_FRONT_Y, WEDGE_Z_START), x_dir=(0,1,0), z_dir=(1,0,0))
wedge_lb_plane = Plane(origin=(INNER_LEFT_X,   INNER_BACK_Y,  WEDGE_Z_START), x_dir=(0,-1,0), z_dir=(1,0,0))

front_plane = Plane(origin=(0, -WIDTH/2 - OVERCUT, TOTAL_HEIGHT), x_dir=(1,0,0), z_dir=(0,1,0))
pin_plane   = Plane.XY.offset(SHEET_T)

# ─── Rib position ─────────────────────────────────────────────
# Top face flush with RING_BASE_TOP_Z, extends downward 0.5mm into base
RIB_RIGHT_X  = RING_INNER_RIGHT_X - RIB_FROM_INNER       # right face X
RIB_CX       = RIB_RIGHT_X - RIB_W / 2                   # centre X
RIB_BOT_Z    = RING_BASE_TOP_Z - RIB_H                   # bottom face Z
RIB_CY       = RING_Y                                     # centre Y (48mm span)

# ─── Through-all cut position ─────────────────────────────────
TCUT_CX = LENGTH / 2 - TCUT_FROM_RIGHT    # = 52.9 − 71.65050 = −18.7505
TCUT_CY = -WIDTH  / 2 + TCUT_FROM_FRONT   # = −40.65 + 35.44150 = −5.2085

# ─────────────────────────────────────────────────────────────
# Scoop geometry: 3 equal horizontal chords of 10.5mm
# All chords level at RING_BASE_TOP_Z → centres directly below midpoints
# Chord for right/left scoops extended by OVERCUT to cleanly exit inner walls
# Cylinder axis = Y, circle in XZ plane
# ─────────────────────────────────────────────────────────────
def _cyl_from_chord_sag(chord, sag):
    """Circle radius and depth-to-centre for horizontal chord + downward sagitta."""
    R = (chord**2 / 4 + sag**2) / (2 * sag)
    cz_below_top = R - sag          # how far below RING_BASE_TOP_Z centre sits
    return R, cz_below_top

# Right scoop: right endpoint exits into wall by OVERCUT
_R_chord = SCOOP_W + OVERCUT        # 10.6mm
_R_R, _R_dz = _cyl_from_chord_sag(_R_chord, SCOOP_SAG)
_R_CX  = RING_INNER_RIGHT_X - SCOOP_W / 2 + OVERCUT / 2   # chord midpoint X
_R_CZ  = RING_BASE_TOP_Z + _R_dz   # centre ABOVE chord → arc dips DOWN into base

# Middle scoop: both endpoints are internal — no OVERCUT needed
_M_chord = SCOOP_W                  # 10.5mm
_M_R, _M_dz = _cyl_from_chord_sag(_M_chord, SCOOP_SAG)
_M_CX  = RING_INNER_RIGHT_X - SCOOP_W - SCOOP_W / 2       # chord midpoint X
_M_CZ  = RING_BASE_TOP_Z + _M_dz   # centre ABOVE chord → arc dips DOWN into base

# Left scoop: left endpoint exits into wall by OVERCUT
_L_chord = SCOOP_W + OVERCUT        # 10.6mm
_L_R, _L_dz = _cyl_from_chord_sag(_L_chord, SCOOP_SAG)
_L_CX  = RING_INNER_LEFT_X + SCOOP_W / 2 - OVERCUT / 2    # chord midpoint X
_L_CZ  = RING_BASE_TOP_Z + _L_dz   # centre ABOVE chord → arc dips DOWN into base

_SCOOP_EXT = RING_INNER_W + 2 * OVERCUT   # Y extrude depth
_WALL_LR   = (RING_OUTER_L - RING_INNER_L) / 2             # 1.0mm wall strip

# ─── Build Tray ───────────────────────────────────────────────
with BuildPart() as tray:
    Box(LENGTH, WIDTH, TOTAL_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.MIN))
    with Locations((0, 0, SHEET_T)):
        Box(CAVITY_L, CAVITY_W, WALL_HEIGHT,
            align=(Align.CENTER, Align.CENTER, Align.MIN), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((X_R, Y_B)): Circle(HOLE_DIA / 2)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((X_L, Y_B)): Circle(HOLE_DIA / 2)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((X_R, Y_T)): Circle(HOLE_DIA / 2)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((X_L, Y_T)): Circle(HOLE_DIA / 2)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(front_plane):
        with Locations((SQ_X1, SQ_SK_Y)): Rectangle(SQUARE_SIZE, SQUARE_SIZE)
    extrude(amount=WALL_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(front_plane):
        with Locations((SQ_X2, SQ_SK_Y)): Rectangle(SQUARE_SIZE, SQUARE_SIZE)
    extrude(amount=WALL_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(front_plane):
        with Locations((SQ_X3, SQ_SK_Y)): Rectangle(SQUARE_SIZE, SQUARE_SIZE)
    extrude(amount=WALL_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(front_plane):
        with Locations((SQ_X4, SQ_SK_Y)): Rectangle(SQUARE_SIZE, SQUARE_SIZE)
    extrude(amount=WALL_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((SLOT1_X, SLOT1_Y)): Rectangle(SLOT1_W, SLOT1_L)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((SLOT2_X, SLOT2_Y)): Rectangle(SLOT2_W, SLOT2_L)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((SLOT3_X, SLOT3_Y)): Rectangle(SLOT3_W, SLOT3_L)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((SLOT4_X, SLOT4_Y)): Rectangle(SLOT4_L, SLOT4_W)
    extrude(amount=SHEET_T + 2*OVERCUT, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((TCUT_CX, TCUT_CY)):
            Rectangle(TCUT_W, TCUT_L)
    extrude(amount=TOTAL_HEIGHT + 2*OVERCUT, mode=Mode.SUBTRACT)

# ─── Build Ring + Base ────────────────────────────────────────
with BuildPart() as ring:
    with BuildSketch(Plane.XY.offset(SHEET_T)):
        with Locations((RING_X, RING_Y)):
            Rectangle(RING_OUTER_L, RING_OUTER_W)
            Rectangle(RING_INNER_L, RING_INNER_W, mode=Mode.SUBTRACT)
    extrude(amount=RING_HEIGHT)
    with BuildSketch(Plane.XY.offset(RING_BASE_Z)):
        with Locations((RING_X, RING_Y)):
            Rectangle(RING_OUTER_L, RING_OUTER_W)
    extrude(amount=RING_BASE_T)

    # ── 3 scoops: cylinder subtract along Y, circle in XZ ────
    with BuildSketch(Plane(origin=(_R_CX, RING_INNER_FRONT_Y - OVERCUT, _R_CZ),
                           x_dir=(1,0,0), z_dir=(0,1,0))):
        Circle(_R_R)
    extrude(amount=_SCOOP_EXT, mode=Mode.SUBTRACT)

    with BuildSketch(Plane(origin=(_M_CX, RING_INNER_FRONT_Y - OVERCUT, _M_CZ),
                           x_dir=(1,0,0), z_dir=(0,1,0))):
        Circle(_M_R)
    extrude(amount=_SCOOP_EXT, mode=Mode.SUBTRACT)

    with BuildSketch(Plane(origin=(_L_CX, RING_INNER_FRONT_Y - OVERCUT, _L_CZ),
                           x_dir=(1,0,0), z_dir=(0,1,0))):
        Circle(_L_R)
    extrude(amount=_SCOOP_EXT, mode=Mode.SUBTRACT)

    # ── Restore right and left walls damaged by cylinder over-reach ───────────
    with BuildSketch(Plane.XY.offset(SHEET_T)):
        with Locations(((RING_INNER_RIGHT_X + RING_RIGHT_EDGE_X) / 2, RING_Y)):
            Rectangle(_WALL_LR, RING_OUTER_W)
    extrude(amount=RING_HEIGHT)
    with BuildSketch(Plane.XY.offset(RING_BASE_Z)):
        with Locations(((RING_INNER_RIGHT_X + RING_RIGHT_EDGE_X) / 2, RING_Y)):
            Rectangle(_WALL_LR, RING_OUTER_W)
    extrude(amount=RING_BASE_T)
    with BuildSketch(Plane.XY.offset(SHEET_T)):
        with Locations(((RING_LEFT_EDGE_X + RING_INNER_LEFT_X) / 2, RING_Y)):
            Rectangle(_WALL_LR, RING_OUTER_W)
    extrude(amount=RING_HEIGHT)
    with BuildSketch(Plane.XY.offset(RING_BASE_Z)):
        with Locations(((RING_LEFT_EDGE_X + RING_INNER_LEFT_X) / 2, RING_Y)):
            Rectangle(_WALL_LR, RING_OUTER_W)
    extrude(amount=RING_BASE_T)

    # ── Rectangular solid: top face flush with base top, 0.5mm into base ──────
    with BuildSketch(Plane.XY.offset(RIB_BOT_Z)):
        with Locations((RIB_CX, RIB_CY)):
            Rectangle(RIB_W, RING_INNER_W)
    extrude(amount=RIB_H)

    # ── Second rectangular solid: left face 9.5mm from RING_INNER_LEFT_X ──────
    with BuildSketch(Plane.XY.offset(RIB_BOT_Z)):
        with Locations((RING_INNER_LEFT_X + RIB_FROM_INNER + RIB_W / 2, RIB_CY)):
            Rectangle(RIB_W, RING_INNER_W)
    extrude(amount=RIB_H)

    # ── Through-all cut (shared with tray) ────────────────────
    with BuildSketch(Plane.XY.offset(-OVERCUT)):
        with Locations((TCUT_CX, TCUT_CY)):
            Rectangle(TCUT_W, TCUT_L)
    extrude(amount=TOTAL_HEIGHT + 2*OVERCUT, mode=Mode.SUBTRACT)

    # ── Front wall holes ──────────────────────────────────────
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H1_CX, RING_HOLE_FY)):
            Rectangle(H1_L, RING_HOLE_W)
    extrude(amount=-(RING_HOLE_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H1_CX, RING_HOLE2_FY)):
            Rectangle(H1_L, RING_HOLE2_W)
    extrude(amount=-(RING_HOLE2_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H3_CX, RING_HOLE_FY)):
            Rectangle(H3_L, RING_HOLE_W)
    extrude(amount=-(RING_HOLE_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H3_CX, RING_HOLE2_FY)):
            Rectangle(H3_L, RING_HOLE2_W)
    extrude(amount=-(RING_HOLE2_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H2_CX, RING_HOLE_FY)):
            Rectangle(H2_L, RING_HOLE_W)
    extrude(amount=-(RING_HOLE3_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H2_CX, RING_HOLE2_FY)):
            Rectangle(H2_L, RING_HOLE2_W)
    extrude(amount=-(RING_HOLE2_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(slant_front_plane):
        with BuildLine():
            Line((H2_CX - H2_L/2,                -RING_HOLE3_Z_BOT),
                 (H2_CX + H2_L/2,                -RING_HOLE3_Z_BOT))
            Line((H2_CX + H2_L/2,                -RING_HOLE3_Z_BOT),
                 (H2_CX + H2_L/2 - SLANT_X_TAPER,-SLANT_Z_BOT))
            Line((H2_CX + H2_L/2 - SLANT_X_TAPER,-SLANT_Z_BOT),
                 (H2_CX - H2_L/2 + SLANT_X_TAPER,-SLANT_Z_BOT))
            Line((H2_CX - H2_L/2 + SLANT_X_TAPER,-SLANT_Z_BOT),
                 (H2_CX - H2_L/2,                -RING_HOLE3_Z_BOT))
        make_face()
    extrude(amount=RING_HOLE_W + 2*OVERCUT, mode=Mode.SUBTRACT)
    with Locations((H2_CX, RING_FRONT_Y + RING_HOLE_W/2, SLANT_Z_BOT - BOTTOM_CUT_D_Z/2)):
        Box(BOTTOM_CUT_W, RING_HOLE_W+2*OVERCUT, BOTTOM_CUT_D_Z+2*OVERCUT,
            align=(Align.CENTER, Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)

    # ── Back wall holes ───────────────────────────────────────
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H5_CX, RING_HOLE_BY)):
            Rectangle(H5_L, RING_HOLE_W)
    extrude(amount=-(RING_HOLE_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H5_CX, RING_HOLE2_BY)):
            Rectangle(H5_L, RING_HOLE2_W)
    extrude(amount=-(RING_HOLE2_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H4_CX, RING_HOLE_BY)):
            Rectangle(H4_L, RING_HOLE_W)
    extrude(amount=-(RING_HOLE3_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H4_CX, RING_HOLE2_BY)):
            Rectangle(H4_L, RING_HOLE2_W)
    extrude(amount=-(RING_HOLE2_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(slant_back_plane):
        with BuildLine():
            Line((H4_CX - H4_L/2,                 RING_HOLE3_Z_BOT),
                 (H4_CX + H4_L/2,                 RING_HOLE3_Z_BOT))
            Line((H4_CX + H4_L/2,                 RING_HOLE3_Z_BOT),
                 (H4_CX + H4_L/2 - SLANT_X_TAPER, SLANT_Z_BOT))
            Line((H4_CX + H4_L/2 - SLANT_X_TAPER, SLANT_Z_BOT),
                 (H4_CX - H4_L/2 + SLANT_X_TAPER, SLANT_Z_BOT))
            Line((H4_CX - H4_L/2 + SLANT_X_TAPER, SLANT_Z_BOT),
                 (H4_CX - H4_L/2,                 RING_HOLE3_Z_BOT))
        make_face()
    extrude(amount=RING_HOLE_W + 2*OVERCUT, mode=Mode.SUBTRACT)
    with Locations((H4_CX, RING_BACK_Y - RING_HOLE_W/2, SLANT_Z_BOT - BOTTOM_CUT_D_Z/2)):
        Box(BOTTOM_CUT_W, RING_HOLE_W+2*OVERCUT, BOTTOM_CUT_D_Z+2*OVERCUT,
            align=(Align.CENTER, Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H6_CX, RING_HOLE_BY)):
            Rectangle(H6_L, RING_HOLE_W)
    extrude(amount=-(RING_HOLE3_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(RING_HOLE_Z_TOP)):
        with Locations((H6_CX, RING_HOLE2_BY)):
            Rectangle(H6_L, RING_HOLE2_W)
    extrude(amount=-(RING_HOLE2_D + 2*OVERCUT), mode=Mode.SUBTRACT)
    with BuildSketch(slant_back_plane):
        with BuildLine():
            Line((H6_CX - H6_L/2,                 RING_HOLE3_Z_BOT),
                 (H6_CX + H6_L/2,                 RING_HOLE3_Z_BOT))
            Line((H6_CX + H6_L/2,                 RING_HOLE3_Z_BOT),
                 (H6_CX + H6_L/2 - SLANT_X_TAPER, SLANT_Z_BOT))
            Line((H6_CX + H6_L/2 - SLANT_X_TAPER, SLANT_Z_BOT),
                 (H6_CX - H6_L/2 + SLANT_X_TAPER, SLANT_Z_BOT))
            Line((H6_CX - H6_L/2 + SLANT_X_TAPER, SLANT_Z_BOT),
                 (H6_CX - H6_L/2,                 RING_HOLE3_Z_BOT))
        make_face()
    extrude(amount=RING_HOLE_W + 2*OVERCUT, mode=Mode.SUBTRACT)
    with Locations((H6_CX, RING_BACK_Y - RING_HOLE_W/2, SLANT_Z_BOT - BOTTOM_CUT_D_Z/2)):
        Box(BOTTOM_CUT_W, RING_HOLE_W+2*OVERCUT, BOTTOM_CUT_D_Z+2*OVERCUT,
            align=(Align.CENTER, Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)

    # ── Square holes ──────────────────────────────────────────
    for sx, sy in [
        (RING_SQ_R_LEFT_X,  SQ_FRONT_Y_CTR), (RING_SQ_R_RIGHT_X, SQ_FRONT_Y_CTR),
        (RING_SQ_L_LEFT_X,  SQ_FRONT_Y_CTR), (RING_SQ_L_RIGHT_X, SQ_FRONT_Y_CTR),
        (RING_SQ3_LEFT_X,   SQ_FRONT_Y_CTR), (RING_SQ3_RIGHT_X,  SQ_FRONT_Y_CTR),
        (RING_SQ_B_LEFT_X,  SQ_BACK_Y_CTR),  (RING_SQ_B_RIGHT_X, SQ_BACK_Y_CTR),
        (RING_SQ_BR_LEFT_X, SQ_BACK_Y_CTR),  (RING_SQ_BR_RIGHT_X,SQ_BACK_Y_CTR),
        (RING_SQ_BL_LEFT_X, SQ_BACK_Y_CTR),  (RING_SQ_BL_RIGHT_X,SQ_BACK_Y_CTR),
    ]:
        with Locations((sx, sy, SQ_HOLE_Z_CTR)):
            Box(SQ_HOLE_SIZE, SQ_HOLE_DEPTH+2*OVERCUT, SQ_HOLE_SIZE,
                align=(Align.CENTER, Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)

# ─── Wedges ───────────────────────────────────────────────────
with BuildPart() as wedge_rf:
    with BuildSketch(wedge_rf_plane):
        with BuildLine():
            Line((0,0),(0,WEDGE_HEIGHT))
            Line((0,WEDGE_HEIGHT),(WEDGE_BASE_W,WEDGE_HEIGHT))
            Line((WEDGE_BASE_W,WEDGE_HEIGHT),(0,0))
        make_face()
    extrude(amount=WEDGE_BASE_L)

with BuildPart() as wedge_rb:
    with BuildSketch(wedge_rb_plane):
        with BuildLine():
            Line((0,0),(0,-WEDGE_HEIGHT))
            Line((0,-WEDGE_HEIGHT),(WEDGE_BASE_W,-WEDGE_HEIGHT))
            Line((WEDGE_BASE_W,-WEDGE_HEIGHT),(0,0))
        make_face()
    extrude(amount=WEDGE_BASE_L)

with BuildPart() as wedge_lf:
    with BuildSketch(wedge_lf_plane):
        with BuildLine():
            Line((0,0),(0,WEDGE_HEIGHT))
            Line((0,WEDGE_HEIGHT),(WEDGE_BASE_W,WEDGE_HEIGHT))
            Line((WEDGE_BASE_W,WEDGE_HEIGHT),(0,0))
        make_face()
    extrude(amount=WEDGE_BASE_L)

with BuildPart() as wedge_lb:
    with BuildSketch(wedge_lb_plane):
        with BuildLine():
            Line((0,0),(0,-WEDGE_HEIGHT))
            Line((0,-WEDGE_HEIGHT),(WEDGE_BASE_W,-WEDGE_HEIGHT))
            Line((WEDGE_BASE_W,-WEDGE_HEIGHT),(0,0))
        make_face()
    extrude(amount=WEDGE_BASE_L)

# ─── Pins ─────────────────────────────────────────────────────
with BuildPart() as pin1:
    with BuildSketch(pin_plane):
        with Locations((PIN1_X, PIN1_Y)): Circle(PIN_DIA / 2)
    extrude(amount=PIN_HEIGHT)

with BuildPart() as pin2:
    with BuildSketch(pin_plane):
        with Locations((PIN2_X, PIN2_Y)): Circle(PIN_DIA / 2)
    extrude(amount=PIN_HEIGHT)

with BuildPart() as pin3:
    with BuildSketch(pin_plane):
        with Locations((PIN3_X, PIN3_Y)): Circle(PIN_DIA / 2)
    extrude(amount=PIN_HEIGHT)

with BuildPart() as pin4:
    with BuildSketch(pin_plane):
        with Locations((PIN4_X, PIN4_Y)): Circle(PIN_DIA / 2)
    extrude(amount=PIN_HEIGHT)

show_all()
