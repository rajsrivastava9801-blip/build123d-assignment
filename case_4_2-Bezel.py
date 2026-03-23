from build123d import *
from ocp_vscode import show, Camera

# ─── Parameters ───────────────────────────────────────────────
OUTER_W      = 81.3       # mm
OUTER_H      = 105.8      # mm
FRAME_T      = 1.0        # mm  flat bezel thickness
WALL_T       = 1.0        # mm  boundary wall thickness (inward)
WALL_DEPTH   = 4.0        # mm  boundary wall depth (downward)

LEDGE_W      = 6.00010        # mm  bottom ledge width
LEDGE_D      = 1.0        # mm  bottom ledge depth

RIGHT_RIB_T  = 0.71490    # mm  right rib thickness
RIGHT_RIB_D  = 1.0        # mm  right rib depth

TOP_RIB_L    = 28.5       # mm  top rib length
TOP_RIB_W    = 6        # mm  top rib width
TOP_RIB_D    = 1.0        # mm  top rib depth

CONN_W       = 1.5        # mm  connector width
CONN_D       = 1.0        # mm  connector depth

PIN_H        = 4.0        # mm  cylinder pin height
PIN_D        = 1.8        # mm  cylinder pin diameter
PIN_OFFSET   = 4.5        # mm  pin centre distance from nearest outer edges

SLOT_W       = 1.8        # mm  inner slot width along X axis
SLOT_L       = 2.8        # mm  inner slot length along Y axis
SLOT_DEPTH   = 0.5        # mm  inner slot cut depth
SLOT_BOT_OFF = 3.1        # mm  bottom edge of slot from lowest outer edge
SLOT_RGT_OFF = 3.6        # mm  right edge of slot from rightmost outer edge

OUTER_SLOT_GAP   = 1.1    # mm  gap between inner and outer slot edges
OUTER_SLOT_DEPTH = 1.5    # mm  from Z = +0.5 mm down to Z = -1.0 mm

INNER_W      = 64.58191   # mm
INNER_H      = 83.93434   # mm
LEFT_OFFSET  = 11.5286    # mm
TOP_OFFSET   = 10.93283   # mm

# ─── Derived inner-cutout centre ──────────────────────────────
inner_cx = (LEFT_OFFSET + INNER_W / 2) - OUTER_W / 2
inner_cy = OUTER_H / 2 - (TOP_OFFSET + INNER_H / 2)

# ─── Derived wall inner face dimensions ───────────────────────
wall_inner_W = OUTER_W - 2 * WALL_T        # 79.3 mm
wall_inner_H = OUTER_H - 2 * WALL_T        # 103.8 mm

# ─── Bottom ledge position ────────────────────────────────────
ledge_cx = 0
ledge_cy = -(wall_inner_H / 2) + (LEDGE_W / 2)

# ─── Right rib position ───────────────────────────────────────
rib_cx = (wall_inner_W / 2) - (RIGHT_RIB_T / 2)
rib_cy = 0

# ─── Top-right rib position ───────────────────────────────────
top_right_rib_cx = (wall_inner_W / 2) - (TOP_RIB_L / 2)
top_right_rib_cy = (wall_inner_H / 2) - (TOP_RIB_W / 2)

# ─── Top-left rib position ────────────────────────────────────
top_left_rib_cx = -(wall_inner_W / 2) + (TOP_RIB_L / 2)
top_left_rib_cy = (wall_inner_H / 2) - (TOP_RIB_W / 2)

# ─── Connector position ───────────────────────────────────────
conn_L  = wall_inner_W - 2 * TOP_RIB_L
conn_cx = 0
conn_cy = (wall_inner_H / 2) - (CONN_W / 2)

# ─── Pin centres (4.5 mm from nearest outer edges) ────────────
pin_x_right =  OUTER_W / 2 - PIN_OFFSET
pin_x_left  = -OUTER_W / 2 + PIN_OFFSET
pin_y_top   =  OUTER_H / 2 - PIN_OFFSET
pin_y_bot   = -OUTER_H / 2 + PIN_OFFSET

# ─── Inner slot centre position ───────────────────────────────
slot_bottom_y = -OUTER_H / 2 + SLOT_BOT_OFF          # -49.8 mm
slot_cy       = slot_bottom_y + SLOT_L / 2            # -48.4 mm
slot_right_x  =  OUTER_W / 2 - SLOT_RGT_OFF          # +37.05 mm
slot_cx       = slot_right_x - SLOT_W / 2             # +36.15 mm

# ─── Outer slot dimensions and centre ─────────────────────────
outer_slot_W  = SLOT_W + 2 * OUTER_SLOT_GAP           # 1.8 + 2.2 = 4.0 mm
outer_slot_L  = SLOT_L + 2 * OUTER_SLOT_GAP           # 2.8 + 2.2 = 5.0 mm
outer_slot_cx = slot_cx                                # same centre X
outer_slot_cy = slot_cy                                # same centre Y

# ─── Build ────────────────────────────────────────────────────
with BuildPart() as frame:

    # 1. Flat bezel face (Z = 0 → +1 mm)
    with BuildSketch(Plane.XY):
        Rectangle(OUTER_W, OUTER_H)
        with Locations((inner_cx, inner_cy)):
            Rectangle(INNER_W, INNER_H, mode=Mode.SUBTRACT)
    extrude(amount=FRAME_T)

    # 2. Boundary wall (Z = 0 → -4 mm)
    with BuildSketch(Plane.XY):
        Rectangle(OUTER_W, OUTER_H)
        Rectangle(wall_inner_W, wall_inner_H, mode=Mode.SUBTRACT)
    extrude(amount=-WALL_DEPTH)

    # 3. Bottom solid ledge (Z = 0 → -1 mm)
    with BuildSketch(Plane.XY):
        with Locations((ledge_cx, ledge_cy)):
            Rectangle(wall_inner_W, LEDGE_W)
    extrude(amount=-LEDGE_D)

    # 4. Right wall rib (Z = 0 → -1 mm)
    with BuildSketch(Plane.XY):
        with Locations((rib_cx, rib_cy)):
            Rectangle(RIGHT_RIB_T, wall_inner_H)
    extrude(amount=-RIGHT_RIB_D)

    # 5. Top-right rib (Z = 0 → -1 mm)
    with BuildSketch(Plane.XY):
        with Locations((top_right_rib_cx, top_right_rib_cy)):
            Rectangle(TOP_RIB_L, TOP_RIB_W)
    extrude(amount=-TOP_RIB_D)

    # 6. Top-left rib (Z = 0 → -1 mm)
    with BuildSketch(Plane.XY):
        with Locations((top_left_rib_cx, top_left_rib_cy)):
            Rectangle(TOP_RIB_L, TOP_RIB_W)
    extrude(amount=-TOP_RIB_D)

    # 7. Top connector rib (Z = 0 → -1 mm)
    with BuildSketch(Plane.XY):
        with Locations((conn_cx, conn_cy)):
            Rectangle(conn_L, CONN_W)
    extrude(amount=-CONN_D)

    # 8. Cylindrical pins (Z = -1 mm → -5 mm)
    with BuildSketch(Plane.XY.offset(-1)):
        with Locations(
            (pin_x_right, pin_y_top),
            (pin_x_left,  pin_y_top),
            (pin_x_left,  pin_y_bot),
        ):
            Circle(PIN_D / 2)
    extrude(amount=-PIN_H)

    # 9. Inner rectangular slot cut (Z = +1 mm → +0.5 mm)
    with BuildSketch(Plane.XY.offset(FRAME_T)):
        with Locations((slot_cx, slot_cy)):
            Rectangle(SLOT_W, SLOT_L)
    extrude(amount=-SLOT_DEPTH, mode=Mode.SUBTRACT)

    # 10. Outer rectangular slot cut (Z = +0.5 mm → -1.0 mm)
    with BuildSketch(Plane.XY.offset(SLOT_DEPTH)):
        with Locations((outer_slot_cx, outer_slot_cy)):
            Rectangle(outer_slot_W, outer_slot_L)
    extrude(amount=-OUTER_SLOT_DEPTH, mode=Mode.SUBTRACT)

# ─── OCP CAD Viewer ───────────────────────────────────────────
show(frame, reset_camera=Camera.RESET)