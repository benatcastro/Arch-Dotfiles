colors = [
        '0x282c32', #black
        '0xe06c75', #red
        '0x98c379', #green
        '0xe5c07b', #yellow
        '0x61afef', #blue
        '0xc678dd', #magente
        '0x56b6c2', #cyan
        '0xdcdfe4'  #white
        ]
print(colors)

screens = [
    Screen(
        bottom=bar.Bar(
            [
            widget.Mpris2(
                name="spotify",
                stop_pause_text="Paused", scroll_chars=None,
                display_metadata=["xesam:title", "xesam:artist"],
                objname="org.mpris.MediaPlayer2.spotify",
                ),
            widget.GroupBox(
                highlight_method='line',
                actve= colors[1],
                ),
            widget.WindowName(),
            widget.CPUGraph(type='line', border_width= 0),
            widget.MemoryGraph(type='line', border_width= 0),
            widget.HDDBusyGraph(type='line', border_width= 0, device = 'nvme0n1'),
            widget.CapsNumLockIndicator(),
            widget.PulseVolume(),
            widget.Clock(timezone='Europe/Madrid', format='%B %-d, %H:%M'),
            ], 50),
        ),
    ]
