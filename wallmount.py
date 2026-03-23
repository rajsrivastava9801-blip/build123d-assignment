from build123d import *
from ocp_vscode import show_all

# Main sheet dimensions
main_L = 59.01716   # X (shorter side)
main_W = 63.0       # Y (longer side)
t      = 2.0        # thickness (Z) — same for all pieces

# Side wall dimensions (as specified)
wall_L = 63.01716   # X — wider than main sheet, creates H legs
wall_W = 10.0       # Y — depth of the side walls

# All top faces at same Z → Z top = +t/2 = +1.0
# All pieces share the same Z center = 0

with BuildPart() as part:

    # ── Main flat sheet (centered at origin) ──────────────────────────────
    # X: [-29.50858, +29.50858]
    # Y: [-31.5,     +31.5    ]
    # Z: [-1,        +1       ]  ← top face at Z=+1
    Box(main_L, main_W, t)

    # ── Side walls at the two short (Y) ends ──────────────────────────────
    # Y center: ±(31.5 + wall_W/2) = ±36.5
    # Z: [-1, +1]  ← same as main sheet → top faces flush ✓
    for sign in [1, -1]:
        with Locations((0, sign * (main_W / 2 + wall_W / 2), 0)):
            Box(wall_L, wall_W, t)

    # ── Hole centres (shared by top & bottom) ─────────────────────────────
    # Distance from shorter side (X edges ±29.50858): 6.52635 mm
    # Distance from longer  side (Y edges ±31.5)    : 6.52251 mm
    hole_x = main_L / 2 - 6.52635   # ±22.98223
    hole_y = main_W / 2 - 6.52251   # ±24.97749

    corners = [
        ( hole_x,  hole_y),
        (-hole_x,  hole_y),
        ( hole_x, -hole_y),
        (-hole_x, -hole_y),
    ]

    # ── Top face: cylindrical hole r=2mm, depth=0.95mm ────────────────────
    # Drills from Z=+1 (top) down to Z=+0.05
    with Locations(*[(cx, cy, t / 2) for cx, cy in corners]):
        Hole(radius=2.0, depth=0.95)

    # ── Bottom face: countersink cone r=3.05mm → r=2mm, height=1.05mm ─────
    # Entry at Z=-1 (bottom face) with r=3.05mm
    # Tip   at Z=+0.05           with r=2.0mm → meets top hole exactly
    # Cone height = t - 0.95 = 1.05mm
    cone_h = t - 0.95   # 1.05 mm

    for cx, cy in corners:
        pln = Plane(
            origin=(cx, cy, -t / 2),
            x_dir=(1, 0, 0),
            z_dir=(0, 0, -1),       # flipped: drill goes upward into part
        )
        with Locations(pln):
            CounterSinkHole(
                radius=2.0,               # narrow end — meets top hole
                counter_sink_radius=3.05, # wide entry at bottom face
                depth=cone_h,             # 1.05 mm total depth
                counter_sink_angle=90,    # 90° included = 45° half-angle
            )                             # (3.05-2.0)/tan(45°) = 1.05mm ✓

    # ── Triangular extrusions at all 4 outer corners ──────────────────────
    # Right-triangle prism on the BOTTOM face, pointing downward (-Z):
    #   Base   : 2mm inward in X (toward centre)
    #   Height : 2mm downward in -Z (away from part)
    #   Length : 10mm in Y — exactly matching & aligned with side wall width
    #
    # Sketch plane sits on the INNER Y face of each side wall end (Y = ±31.5)
    # normal pointing outward in Y, extruded 10mm to match wall width.
    #
    # Local coord system:
    #   x_dir = (-sx, 0, 0)  → local +X points inward (toward X=0)
    #   z_dir = (0, sy, 0)   → normal / extrude direction (outward Y)
    #   local Y = z_dir × x_dir = (0, 0, sx*sy)
    #     sx*sy=+1 → local Y = +Z (world up)
    #     sx*sy=-1 → local Y = -Z (world down)
    # To go DOWNWARD we use vertex (0, -height_sign * t)

    wall_end_x   = wall_L / 2      # ±31.50858
    wall_inner_y = main_W / 2      # ±31.5

    for sx in [1, -1]:
        for sy in [1, -1]:
            height_sign = sy * sx   # controls which local Y = world -Z
            pln = Plane(
                origin=(sx * wall_end_x, sy * wall_inner_y, -t / 2),
                x_dir=(-sx, 0, 0),
                z_dir=(0, sy, 0),
            )
            with BuildSketch(pln):
                with BuildLine():
                    Polyline([
                        (0, 0),                     # right-angle: outer X, bottom Z
                        (t, 0),                     # 2mm inward X (base leg)
                        (0, -height_sign * t),      # 2mm DOWNWARD in -Z (height leg)
                        (0, 0),
                    ])
                make_face()
            extrude(amount=wall_W)              # 10mm outward in Y = wall width ✓

    # ── Trapezoidal extrusions at 4 outer corners ─────────────────────────
    # Cross-section (X-Z plane, sx=+1):
    #
    #  Z=0    ● pts[0]                         ← top of 11.7mm (at wall_end_x, Z=0)
    #         │ ╲  45° slant
    # 11.7mm  │   ╲
    #         │     ╲
    # Z=-7.84 │       ● pts[3]  (wall_end_x+7.84, Z=-7.84) ← top of 3.86mm
    #         │       │ 3.86mm (extends beyond boundary)
    # Z=-11.7 ● pts[1]─● pts[2]  ← 7.84mm horizontal BOTTOM (toward bottom face) ✓
    #   (wall_end_x)  (wall_end_x+7.84)
    #
    # pts[0]: (wall_end_x,      Z=0    )  top of 11.7mm — coincident with outer wall ✓
    # pts[1]: (wall_end_x,      Z=-11.7)  bottom of 11.7mm
    # pts[2]: (wall_end_x+7.84, Z=-11.7)  bottom of 3.86mm — 7.84mm horiz bottom ✓
    # pts[3]: (wall_end_x+7.84, Z=-3.86)  top of 3.86mm face
    # Slant pts[0]→pts[3]: Δx=+7.84, Δz=-7.84 → 45° ✓

    trap_h    = 11.7   # tall face — coincident with outer wall face ✓
    trap_s    = 3.86   # short face — extends beyond boundary
    trap_perp = 7.84   # = trap_h - trap_s

    for sx in [1, -1]:
        for sy in [1, -1]:
            depth_sign = sx * sy   # maps local_y to world -Z

            pln = Plane(
                origin=(sx * wall_end_x, sy * wall_inner_y, 0),
                x_dir=(sx, 0, 0),       # local +x → outward world X
                z_dir=(0, sy, 0),       # normal/extrude → outward world Y
            )
            pts = [
                (0,         0                    ),  # pts[0] top of 11.7mm  Z=0
                (0,         trap_h * depth_sign  ),  # pts[1] bot of 11.7mm  Z=-11.7
                (trap_perp, trap_h * depth_sign  ),  # pts[2] bot of 3.86mm  Z=-11.7  ← 7.84mm horiz bottom ✓
                (trap_perp, trap_perp * depth_sign),  # pts[3] top of 3.86mm  Z=-7.84 → slant Δx=Δz=7.84 → 45° ✓
            ]
            # slant pts[0]→pts[3]: Δlx=+7.84, Δlz=trap_s*depth_sign → 45° ✓
            # 11.7mm face at local_x=0 (world X=wall_end_x) — coincident with outer wall ✓
            # 7.84mm face at bottom Z=-11.7 — toward bottom face ✓
            # 3.86mm face beyond boundary at local_x=7.84 ✓

            with BuildSketch(pln):
                with BuildLine():
                    Polyline(pts + [pts[0]])
                make_face()
            extrude(amount=wall_W)
show_all()