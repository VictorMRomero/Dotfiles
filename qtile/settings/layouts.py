from libqtile import layout
from libqtile.config import Match
from .theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['c8'][0],
    'border_width': 1,
    'margin': 6,
    'single_border_width': 0,
    'single_margin': 10,
}

layouts = [
    layout.Max(),
    layout.MonadTall(
        **layout_conf,  
        change_ratio = 0.02,
        min_ratio = 0.30,
        max_ratio = 0.70,
    ),
    #layout.MonadWide(**layout_conf),
    #layout.Bsp(**layout_conf),
    #layout.Matrix(columns=2, **layout_conf),
    #layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["c8"][0]
)