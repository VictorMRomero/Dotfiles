from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=2)


def icon(fg='text', bg='dark', fontsize=10, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="color5"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=30,
        padding=-3
    )

def powerlineInvertida(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=30,
        padding=-3
    )
def powerlineMiddle(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=30,
        padding=-3        
    )



def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='col1', bg='c11'),
            font='Hack Nerd Font',
            fontsize=18,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['col8'],
            inactive=colors['c10'],
            rounded=False,
            highlight_method='line',
            urgent_alert_method='line',
            urgent_border=colors['col1'],
            this_current_screen_border=colors['col1'],
            this_screen_border=colors['col4'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        )
    ]


primary_widgets = [
    powerline('c6', 'dark'),
    widget.Clock(**base(bg='c6',fg='dark'), format='%I ',fontsize=23),
    widget.Clock(**base(bg='c6',fg='dark'), format='%M '),
    powerlineInvertida('c6', 'dark'),
    icon(bg="dark",fg='c10', text=''),
    powerline('c11', 'dark'),
    *workspaces(),
    powerlineInvertida('c11', 'dark'),

    



    separator(),
    widget.WindowName(**base(fg='col10'), fontsize=14, padding=5, font='Hack Nerd Font',),
    separator(),


    powerline('col4', 'dark'),
    widget.CurrentLayoutIcon(**base('dark','col4'), scale=0.7),
    widget.CurrentLayout(**base('dark','col4'), padding=1),
    powerlineInvertida('col4', 'dark'),
    

    icon(bg="dark",fg='c10', text=''),

    powerline('col5', 'dark'),
    icon(bg="col5", fg='dark', text='', fontsize=15),
    widget.Battery(**base(bg='col5',fg='dark'), format = '{percent:2.0%}' ),

    powerlineMiddle('col6', 'col5'),

    icon(bg="col6", fg='dark', text='', fontsize=30), 
    widget.PulseVolume(**base(bg='col6',fg='dark')),
    
    powerlineMiddle('col7', 'col6'),

    icon(bg="col7",fg='dark', text='', fontsize=25), 
    widget.Clock(**base(bg='col7', fg='dark'), format='%d'),

    powerlineInvertida('col7', 'dark'),

    icon(bg="dark",fg='c10', text=''),

    powerline('inactive', 'dark'),

    widget.Systray(background=colors['inactive'], padding=5),
    powerlineInvertida('inactive', 'dark'),


]


secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %I:%M'),

    powerline('dark', 'color2'),

]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 13,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()

