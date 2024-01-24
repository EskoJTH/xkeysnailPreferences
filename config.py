# -*- coding: utf-8 -*-

keymap("jetbrains-idea", {
    # K("M-KEY_102ND"): K("C-home"),
    # K("M-LShift-KEY_102ND"): K("C-end"),

    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    K("C-b"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    K("C-d"): [K("delete"), set_mark(False)],
    K("LAlt-d"): [K("C-delete"), set_mark(False)]
    
    # K("C-h"): with_mark(K("backspace"))
    # K("LAlt-p"): K("C-page_up"),
    # K("LAlt-n"): K("C-page_down"),
}, when = wm_class_match(r"jetbrains-idea"))


# Keybindings for Firefox/Chrome
keymap( "Default custom bindings", {

    #Ctrl+Alt+j/k to switch next/previous tab
    K("LAlt-KEY_102ND"): K("C-home"),
    K("LAlt-LShift-KEY_102ND"): K("C-end"),
    #K("LAlt-S-MUHENKAN"): K("C-end"),
    K("LAlt-p"): K("C-page_up"),
    K("LAlt-n"): K("C-page_down"),
     #Type C-j to focus to the content
    K("C-l"): K("C-f6"),
     #very naive "Edit in editor" feature (just an example)
    #K("C-LAlt-e"): [K("C-a"), K("C-c"), launch(["emacs"]), sleep(0.5), K("C-v")],
    #nowork

    K("LAlt-Shift-p"): K("C-Shift-page_up"),
    K("LAlt-Shift-n"): K("C-Shift-page_down"),

    K("LAlt-C-p"): K("LAlt-left"),
    K("LAlt-C-n"): K("LAlt-right"),

    K("LAlt-z"): K("C-f4"),
    
        
    K("C-b"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    K("C-h"): with_mark(K("backspace")),
    # Forward/Backward word
    K("LAlt-b"): with_mark(K("C-left")),
    K("LAlt-f"): with_mark(K("C-right")),
    # Beginning/End of lineblood flows bet
    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    # Page up/down
    K("LAlt-v"): with_mark(K("page_up")),
    K("C-v"): with_mark(K("page_down")),
    # Beginning/End of file
    K("LAlt-Shift-comma"): with_mark(K("C-home")),
    K("LAlt-Shift-dot"): with_mark(K("C-end")),
    # Newline
    K("C-m"): K("enter"),
    K("C-j"): K("enter"),
    K("C-o"): [K("enter"), K("left")],
    # Copy
    K("C-w"): [K("C-x"), set_mark(False)],
    K("LAlt-w"): [K("C-c"), set_mark(False)],
    K("C-y"): [K("C-v"), set_mark(False)],
    # Delete
    K("C-d"): [K("delete"), set_mark(False)],
    K("LAlt-d"): [K("C-delete"), set_mark(False)],
    # Backspace
    K("C-SEMICOLON"): [K("backspace"), set_mark(False)], #semicolon = ö?
    K("LAlt-SEMICOLON"): [K("C-backspace"), set_mark(False)],
    # Kill line
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Undo
    K("C-slash"): [K("C-z"), set_mark(False)],
    K("C-Shift-ro"): K("C-z"),
    # Mark
    K("C-space"): set_mark(True),
    K("C-LAlt-space"): with_or_set_mark(K("C-right")),
    # Search
    K("C-s"): [K("F3"), K("C-f")],
    K("C-r"): K("Shift-F3"),
    K("LAlt-Shift-key_5"): K("C-h"),
    # Cancel
    K("C-g"): [K("esc"), set_mark(False)],
    # Escape
    K("C-q"): escape_next_key,
    # C-x YYY
    K("C-x"): {
        # C-x h (select all)
        K("h"): [K("C-home"), K("C-a"), set_mark(True)],
        # C-x C-f (open)
        K("C-f"): K("C-o"),
        # C-x C-s (save)
        K("C-s"): K("C-s"),
        # C-x k (kill tab)
        K("k"): K("C-f4"),
        # C-x C-c (exit)
        K("C-c"): K("C-q"),
        # cancel ?
        K("C-g"): K("C-g"),
        # C-x u (undo)
        K("u"): [K("C-z"), set_mark(False)],
        K("C-b"): K("C-Shift-o"),
        K("C-h"): [K("C-Shift-h")]
    }
    #K("ALT"): K("reserved")

    
}, when = wm_class_match(r"firefox|Arduino|Firefox|Google-chrome|Slack|rocketchat-desktop|libreoffice|Riot|Postman|chromium|Spectral|Telegram|OpenSCAD|Zoom|Meld|meld"))

