@namespace
class SpriteKind:
    slurp = SpriteKind.create()
    minis = SpriteKind.create()
    bandages = SpriteKind.create()
    Big_pot = SpriteKind.create()
    Medkit = SpriteKind.create()

def on_b_pressed():
    global direction
    if direction == 0:
        Player_sprite.set_image(img("""
            . . . 3 3 3 3 3 3 3 . 
                        . . 3 . . . . . . . 3 
                        . . 3 . 3 . . . 3 . 3 
                        . . 3 . . . . . . . 3 
                        . . 3 . 3 . . . 3 . 3 
                        . . 3 . . 3 3 3 . . 3 
                        . . 3 . . . . . . . 3 
                        . . . 3 3 3 3 3 3 3 . 
                        5 5 . . . . 3 . . . . 
                        . 5 3 3 3 3 3 3 3 3 3 
                        . . . . . . 3 . . . . 
                        . . . . . 3 . 3 . . .
        """))
        direction = 1
    else:
        Player_sprite.set_image(img("""
                        . 3 3 3 3 3 3 3 . . . . 
                        3 . . . . . . . 3 . . . 
                        3 . 3 . . . 3 . 3 . . . 
                        3 . . . . . . . 3 . . . 
                        3 . 3 . . . 3 . 3 . . . 
                        3 . . 3 3 3 . . 3 . . . 
                        3 . . . . . . . 3 . . . 
                        . 3 3 3 3 3 3 3 . . . . 
                        . . . . 3 . . . . 5 5 5 
                        3 3 3 3 3 3 3 3 3 5 . . 
                        . . . . 3 . . . . . . . 
                        . . . 3 . 3 . . . . . .
        """))
        direction = 0
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite, otherSprite):
    global Hp
    Hp = 100
    sprites.destroy(sprite)
sprites.on_overlap(SpriteKind.Medkit, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global Hp
    if Hp > 60 and Hp < 75:
        Hp = 75
    elif Hp < 75:
        Hp += 15
    sprites.destroy(sprite2)
sprites.on_overlap(SpriteKind.bandages, SpriteKind.player, on_on_overlap2)

def on_a_pressed():
    global projectile
    controller.vibrate(50)
    scene.camera_shake(2, 100)
    music.play(music.create_song(assets.song("""
            shoot
        """)),
        music.PlaybackMode.IN_BACKGROUND)
    if direction == 0:
        projectile = sprites.create_projectile_from_sprite(img("""
            3 3 3 3
        """), Player_sprite, 125, 0)
    else:
        projectile = sprites.create_projectile_from_sprite(img("""
            3 3 3 3
        """), Player_sprite, -125, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite3, otherSprite3):
    global placement
    if sprite3.lifespan > 500:
        if placement > 10:
            placement += -1
        info.change_score_by(1)
        sprites.destroy(otherSprite3)
        sprite3.lifespan = 500
        sprite3.follow(Player_sprite, 0)
        if sprite3.x < Player_sprite.x:
            sprite3.set_image(img("""
                . 8 8 8 . 8 8 8 . 8 8 8 . 
                                . . . 8 . 8 . 8 . 8 . 8 . 
                                . 8 8 8 . 8 . 8 . 8 . 8 . 
                                . 8 . . . 8 . 8 . 8 . 8 . 
                                . 8 8 8 . 8 8 8 . 8 8 8 . 
                                . . . . . . . . . . . . . 
                                . . . . . . . . . 5 . . . 
                                . . . . . . . . . 5 . . . 
                                . . . . . . . . . 5 5 . . 
                                . 3 3 3 3 3 3 3 . . 3 . . 
                                3 2 . 2 . . . . 3 . 3 . . 
                                3 . 2 . . . 3 . 3 . 3 . . 
                                3 2 . 2 . 3 . . 3 . 3 . 3 
                                3 . . . . 3 . . 3 3 3 3 . 
                                3 2 . 2 . 3 . . 3 . 3 . 3 
                                3 . 2 . . . 3 . 3 . 3 . . 
                                3 2 . 2 . . . . 3 . 3 . . 
                                . 3 3 3 3 3 3 3 . . 3 . .
            """))
        else:
            sprite3.set_image(img("""
                . 8 8 8 . 8 8 8 . 8 8 8 . 
                                . . . 8 . 8 . 8 . 8 . 8 . 
                                . 8 8 8 . 8 . 8 . 8 . 8 . 
                                . 8 . . . 8 . 8 . 8 . 8 . 
                                . 8 8 8 . 8 8 8 . 8 8 8 . 
                                . . . . . . . . . . . . . 
                                . . . 5 . . . . . . . . . 
                                . . . 5 . . . . . . . . . 
                                . . 5 5 . . . . . . . . . 
                                . . 3 . . 3 3 3 3 3 3 3 . 
                                . . 3 . 3 . . . . 2 . 2 3 
                                . . 3 . 3 . 3 . . . 2 . 3 
                                3 . 3 . 3 . . 3 . 2 . 2 3 
                                . 3 3 3 3 . . 3 . . . . 3 
                                3 . 3 . 3 . . 3 . 2 . 2 3 
                                . . 3 . 3 . 3 . . . 2 . 3 
                                . . 3 . 3 . . . . 2 . 2 3 
                                . . 3 . . 3 3 3 3 3 3 3 .
            """))
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap3)

def on_countdown_end():
    game.set_game_over_message(True, "Number #1 victory royal!")
    game.game_over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap4(sprite4, otherSprite4):
    global slurp_amount
    slurp_amount += 75
    sprites.destroy(sprite4)
sprites.on_overlap(SpriteKind.slurp, SpriteKind.player, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    global shield, Hp, player_I_frames
    if funny_stuff == 0 and player_I_frames == 0 and sprite5.lifespan > 500:
        if shield > 0:
            shield += enemy_damage
        elif Hp > 0:
            Hp += enemy_damage
        else:
            game.set_game_over_playable(False,
                music.create_song(assets.song("""
                    death
                """)),
                False)
            game.set_game_over_message(False, "You were placed #" + str(placement))
            game.game_over(False)
        controller.vibrate(200)
        scene.camera_shake(5, 100)
        player_I_frames += 1
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap5)

def on_overlap_tile(sprite6, location):
    if sprite6.lifespan > 500:
        if sprite6.x < Player_sprite.x:
            sprite6.set_image(assets.image("""
                myImage
            """))
        else:
            sprite6.set_image(assets.image("""
                myImage0
            """))
scene.on_overlap_tile(SpriteKind.enemy, sprites.castle.tile_path5, on_overlap_tile)

def on_on_overlap6(sprite7, otherSprite6):
    global shield
    if shield > 25 and shield < 50:
        shield = 50
    elif shield < 50:
        shield += 25
    sprites.destroy(sprite7)
sprites.on_overlap(SpriteKind.minis, SpriteKind.player, on_on_overlap6)

def on_on_overlap7(sprite8, otherSprite7):
    global shield
    shield += 50
    sprites.destroy(sprite8)
sprites.on_overlap(SpriteKind.Big_pot, SpriteKind.player, on_on_overlap7)

def on_combos_attach_combo():
    global Hp, shield, funny_stuff
    if game.ask_for_string("Enter password", 8) == "password":
        game.splash("inf hp/sheild unlocked")
        Hp = 100
        shield = 100
        funny_stuff = 1
        info.stop_countdown()
    else:
        game.splash("Try again!", "Hint: Literally do it")
controller.combos.attach_combo("ududab", on_combos_attach_combo)

healing_items: Sprite = None
Enemy_sprite: Sprite = None
slurp_amount = 0
projectile: Sprite = None
player_I_frames = 0
enemy_damage = 0
placement = 0
shield = 0
Hp = 0
funny_stuff = 0
direction = 0
Player_sprite: Sprite = None
Player_sprite = sprites.create(img("""
        . 3 3 3 3 3 3 3 . . . . 
            3 . . . . . . . 3 . . . 
            3 . 3 . . . 3 . 3 . . . 
            3 . . . . . . . 3 . . . 
            3 . 3 . . . 3 . 3 . . . 
            3 . . 3 3 3 . . 3 . . . 
            3 . . . . . . . 3 . . . 
            . 3 3 3 3 3 3 3 . . . . 
            . . . . 3 . . . . 5 5 5 
            3 3 3 3 3 3 3 3 3 5 . . 
            . . . . 3 . . . . . . . 
            . . . 3 . 3 . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Player_sprite)
scene.camera_follow_sprite(Player_sprite)
tiles.set_current_tilemap(tilemap("""
    level0
"""))
# 0 = right
# 1 = left
direction = 0
tiles.place_on_tile(Player_sprite,
    tiles.get_tile_location(randint(1, 18), randint(1, 18)))
info.set_score(0)
funny_stuff = 0
Hp = 100
shield = 0
placement = 100
statusbar = statusbars.create(30, 6, StatusBarKind.health)
status_bar_shield = statusbars.create(30, 6, StatusBarKind.health)
statusbar.set_bar_border(1, 15)
status_bar_shield.set_bar_border(1, 15)
status_bar_shield.set_color(9, 15, 8)
statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
status_bar_shield.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
statusbar.set_status_bar_flag(StatusBarFlag.IGNORE_VALUE_EVENTS, True)
status_bar_shield.set_status_bar_flag(StatusBarFlag.IGNORE_VALUE_EVENTS, True)
statusbar.set_status_bar_flag(StatusBarFlag.HIDE_TARGET_PREVIEW, True)
status_bar_shield.set_status_bar_flag(StatusBarFlag.HIDE_TARGET_PREVIEW, True)
statusbar.set_status_bar_flag(StatusBarFlag.LABEL_AT_END, True)
status_bar_shield.set_status_bar_flag(StatusBarFlag.LABEL_AT_END, True)
if game.ask_for_string("Do you want a timer (type y for Yes)", 1) == "y":
    info.start_countdown(game.ask_for_number("How long?"))
if game.ask_for_string("Do you want hard mode (type y for Yes)", 1) == "y":
    enemy_damage = -3
else:
    enemy_damage = -1
player_I_frames = 100
game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)

def on_update_interval():
    global Enemy_sprite
    Enemy_sprite = sprites.create(assets.image("""
        myImage
    """), SpriteKind.enemy)
    tiles.place_on_tile(Enemy_sprite,
        tiles.get_tile_location(randint(1, 18), randint(1, 18)))
    Enemy_sprite.follow(Player_sprite, 50)
    Enemy_sprite.lifespan = 100000000000
game.on_update_interval(placement * 10, on_update_interval)

def on_update_interval2():
    global healing_items
    if Math.percent_chance(10):
        healing_items = sprites.create(img("""
                . . e e e . . 
                            . f f f f f . 
                            f 7 7 7 7 7 f 
                            f 7 7 7 7 7 f 
                            f 7 7 7 7 7 f 
                            f 7 7 7 7 7 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            . f f f f f .
            """),
            SpriteKind.slurp)
    elif Math.percent_chance(15):
        healing_items = sprites.create(img("""
                . . e e e . . 
                            . f f f f f . 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            f 9 9 9 9 9 f 
                            . f f f f f .
            """),
            SpriteKind.Big_pot)
    elif Math.percent_chance(25):
        healing_items = sprites.create(img("""
                . 1 1 2 2 2 1 1 . 
                            1 1 1 2 2 2 1 1 1 
                            1 1 2 2 1 2 2 1 1 
                            1 1 2 1 1 1 2 1 1 
                            1 1 2 2 1 2 2 1 1 
                            1 1 1 2 2 2 1 1 1 
                            . 1 1 2 2 2 1 1 .
            """),
            SpriteKind.Medkit)
    elif Math.percent_chance(40):
        healing_items = sprites.create(img("""
                . e e . 
                            . f f . 
                            f 9 9 f 
                            f 9 9 f 
                            f 9 9 f 
                            f 9 9 f 
                            . f f .
            """),
            SpriteKind.minis)
    elif Math.percent_chance(55):
        healing_items = sprites.create(img("""
                . 1 d 1 1 1 1 1 d 1 . 
                            1 1 d 1 1 2 1 1 d 1 1 
                            1 1 d 1 2 2 2 1 d 1 1 
                            1 1 d 1 1 2 1 1 d 1 1 
                            . 1 d 1 1 1 1 1 d 1 .
            """),
            SpriteKind.bandages)
    tiles.place_on_tile(healing_items,
        tiles.get_tile_location(randint(1, 18), randint(1, 18)))
game.on_update_interval(6500, on_update_interval2)

def on_forever():
    if Hp >= 100:
        statusbar.set_position(26, 116)
    elif Hp >= 10:
        statusbar.set_position(23, 116)
    else:
        statusbar.set_position(20, 116)
    if shield >= 100:
        status_bar_shield.set_position(26, 109)
    elif shield >= 10:
        status_bar_shield.set_position(23, 109)
    else:
        status_bar_shield.set_position(20, 109)
forever(on_forever)

def on_forever2():
    global player_I_frames
    if player_I_frames > 0:
        player_I_frames += -1
forever(on_forever2)

def on_forever3():
    global Hp, shield
    if Hp > 100:
        Hp = 100
    if shield > 100:
        shield = 100
forever(on_forever3)

def on_forever4():
    statusbar.value = Hp
    status_bar_shield.value = shield
    status_bar_shield.set_label(convert_to_text(shield), 1)
    if Hp >= 60:
        statusbar.set_color(7, 15, 2)
    elif Hp >= 40:
        statusbar.set_color(5, 15, 2)
    elif Hp > 20:
        statusbar.set_color(4, 15, 2)
    else:
        statusbar.set_color(2, 15, 2)
    if Hp > 20:
        statusbar.set_label(convert_to_text(Hp), 1)
    else:
        statusbar.set_label(convert_to_text(Hp), 2)
forever(on_forever4)

def on_update_interval3():
    global Hp, slurp_amount, shield
    if slurp_amount > 1 and Hp < 100:
        Hp += 1
        slurp_amount += -1
    elif slurp_amount > 1 and Hp >= 100:
        shield += 1
        slurp_amount += -1
game.on_update_interval(100, on_update_interval3)
