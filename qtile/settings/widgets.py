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


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="color5"):
    return widget.TextBox(
        **base(fg, bg),
        text=" ", # Icon: nf-oct-triangle_left
        fontsize=30,
        padding=-3
    )

def powerlineInvertida(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text=" ", # Icon: nf-oct-triangle_left
        fontsize=30,
        padding=-3
    )
def powerlineMiddle(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-3        
    )



def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='col1', bg='c11'),
            font='UbuntuMono Nerd Font',
            fontsize=17,
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
    icon(bg="c6", text=' ', fontsize = 20),
    powerlineInvertida('c6', 'dark'),

    powerline('c11', 'dark'),
    *workspaces(),
    powerlineInvertida('c11', 'dark'),

    icon(bg="dark",fg='c10', text=''),

    powerline('col7', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='col7',fg='dark'), scale=0.65),
    widget.CurrentLayout(**base(bg='col7',fg='dark'), padding=4),

    powerlineMiddle('col4','col7'),

    icon(bg="col4",fg='dark', text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        background=colors['col4'],
        colour_have_updates=colors['dark'],
        colour_no_updates=colors['dark'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),
    powerlineInvertida('col4', 'dark'),

    separator(),
    widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
    separator(),



    



    powerline('col5', 'dark'),
    icon(bg="col5", fg='dark', text=''),
    widget.Battery(**base(bg='col5',fg='dark'), format = '{percent:2.0%}' ),

    powerlineMiddle('col6', 'col5'),

    icon(bg="col6", fg='dark', text=''), # Icon: nf-mdi-calendar_clock 
    widget.Volume(**base(bg='col6',fg='dark')),
    
    powerlineMiddle('col7', 'col6'),

    icon(bg="col7",fg='dark', text=' '), 
    widget.Clock(**base(bg='col7', fg='dark'), format='%d'),

    powerlineInvertida('col7', 'dark'),

    icon(bg="dark",fg='c10', text=''),

    powerline('col9', 'dark'),

    widget.Systray(background=colors['col9'], padding=5),
    powerlineInvertida('col9', 'dark'),

    icon(bg="dark",fg='c10', text=''),
    
    powerline('col10', 'dark'),
    icon(bg="col10",fg='dark', text=' '), 
    widget.Clock(**base(bg='col10',fg='dark'), format='%I:%M '),
    
    powerlineInvertida('col10', 'dark'),
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

