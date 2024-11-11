namespace SpriteKind {
    export const slurp = SpriteKind.create()
    export const minis = SpriteKind.create()
    export const bandages = SpriteKind.create()
    export const Big_pot = SpriteKind.create()
    export const Medkit = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (direction == 0) {
        Player_sprite.setImage(img`
            . . . f f f f f f f . 
            . . f 1 1 1 1 1 1 1 f 
            . . f 1 f 1 1 1 f 1 f 
            . . f 1 1 1 1 1 1 1 f 
            . . f 1 f 1 1 1 f 1 f 
            . . f 1 1 f f f 1 1 f 
            . . f 1 1 1 1 1 1 1 f 
            . . . f f f f f f f . 
            5 5 . . . . f . . . . 
            . 5 f f f f f f f f f 
            . . . . . . f . . . . 
            . . . . . f . f . . . 
            `)
        direction = 1
    } else {
        Player_sprite.setImage(img`
            . f f f f f f f . . . . 
            f 1 1 1 1 1 1 1 f . . . 
            f 1 f 1 1 1 f 1 f . . . 
            f 1 1 1 1 1 1 1 f . . . 
            f 1 f 1 1 1 f 1 f . . . 
            f 1 1 f f f 1 1 f . . . 
            f 1 1 1 1 1 1 1 f . . . 
            . f f f f f f f . . . . 
            . . . . f . . . . 5 5 5 
            f f f f f f f f f 5 . . 
            . . . . f . . . . . . . 
            . . . f . f . . . . . . 
            `)
        direction = 0
    }
})
sprites.onOverlap(SpriteKind.Medkit, SpriteKind.Player, function (sprite, otherSprite) {
    Hp = 100
    sprites.destroy(sprite)
})
sprites.onOverlap(SpriteKind.bandages, SpriteKind.Player, function (sprite, otherSprite) {
    if (Hp > 60 && Hp < 75) {
        Hp = 75
    } else if (Hp < 75) {
        Hp += 15
    }
    sprites.destroy(sprite)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.vibrate(50)
    scene.cameraShake(2, 100)
    music.play(music.createSong(assets.song`shoot`), music.PlaybackMode.InBackground)
    if (direction == 0) {
        projectile = sprites.createProjectileFromSprite(img`
            f f f f 
            `, Player_sprite, 125, 0)
    } else {
        projectile = sprites.createProjectileFromSprite(img`
            f f f f 
            `, Player_sprite, -125, 0)
    }
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite5, otherSprite5) {
	
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    if (sprite.lifespan > 500) {
        if (placement > 10) {
            placement += -1
        }
        info.changeScoreBy(1)
        sprites.destroy(otherSprite)
        sprite.lifespan = 500
        sprite.follow(Player_sprite, 0)
        if (sprite.x < Player_sprite.x) {
            sprite.setImage(img`
                . 8 8 8 . 8 8 8 . 8 8 8 . 
                . . . 8 . 8 . 8 . 8 . 8 . 
                . 8 8 8 . 8 . 8 . 8 . 8 . 
                . 8 . . . 8 . 8 . 8 . 8 . 
                . 8 8 8 . 8 8 8 . 8 8 8 . 
                . . . . . . . . . 4 . . . 
                . . . . . . . . . 5 . . . 
                . . . . . . . . . 5 4 . . 
                . . . . . . . . . 5 5 5 . 
                . f f f f f f f . . f . . 
                f 2 1 2 1 1 1 1 f . f . . 
                f 1 2 1 1 1 f 1 f . f . . 
                f 2 1 2 1 f 1 1 f . f . f 
                f 1 1 1 1 f 1 1 f f f f . 
                f 2 1 2 1 f 1 1 f . f . f 
                f 1 2 1 1 1 f 1 f . f . . 
                f 2 1 2 1 1 1 1 f . f . . 
                . f f f f f f f . . f . . 
                `)
        } else {
            sprite.setImage(img`
                . 8 8 8 . 8 8 8 . 8 8 8 . 
                . . . 8 . 8 . 8 . 8 . 8 . 
                . 8 8 8 . 8 . 8 . 8 . 8 . 
                . 8 . . . 8 . 8 . 8 . 8 . 
                . 8 8 8 . 8 8 8 . 8 8 8 . 
                . . . . . . . . . . . . . 
                . . . 5 . . . . . . . . . 
                . . . 5 . . . . . . . . . 
                . . 5 5 . . . . . . . . . 
                . . f . . f f f f f f f . 
                . . f . f 1 1 1 1 2 1 2 f 
                . . f . f 1 f 1 1 1 2 1 f 
                f . f . f 1 1 f 1 2 1 2 f 
                . f f f f 1 1 f 1 1 1 1 f 
                f . f . f 1 1 f 1 2 1 2 f 
                . . f . f 1 f 1 1 1 2 1 f 
                . . f . f 1 1 1 1 2 1 2 f 
                . . f . . f f f f f f f . 
                `)
        }
    }
})
info.onCountdownEnd(function () {
    game.reset()
})
sprites.onOverlap(SpriteKind.slurp, SpriteKind.Player, function (sprite, otherSprite) {
    slurp_amount += 75
    sprites.destroy(sprite)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    if (funny_stuff == 0 && player_I_frames == 0 && sprite.lifespan > 500) {
        if (shield > 0) {
            shield += enemy_damage
        } else if (Hp > 0) {
            Hp += enemy_damage
        } else {
            game.setGameOverPlayable(false, music.createSong(assets.song`death`), false)
            game.setGameOverMessage(false, "You were placed #" + ("" + placement))
            game.gameOver(false)
        }
        controller.vibrate(200)
        scene.cameraShake(5, 100)
        player_I_frames += 1
    }
})
scene.onOverlapTile(SpriteKind.Enemy, sprites.castle.tilePath5, function (sprite, location) {
    if (sprite.lifespan > 500) {
        if (sprite.x < Player_sprite.x) {
            sprite.setImage(assets.image`myImage`)
        } else {
            sprite.setImage(assets.image`myImage0`)
        }
    }
})
sprites.onOverlap(SpriteKind.minis, SpriteKind.Player, function (sprite, otherSprite) {
    if (shield > 25 && shield < 50) {
        shield = 50
    } else if (shield < 50) {
        shield += 25
    }
    sprites.destroy(sprite)
})
sprites.onOverlap(SpriteKind.Big_pot, SpriteKind.Player, function (sprite, otherSprite) {
    shield += 50
    sprites.destroy(sprite)
})
controller.combos.attachCombo("ududab", function () {
    if (game.askForString("Enter password", 8) == "password") {
        game.splash("inf hp/sheild unlocked")
        Hp = 100
        shield = 100
        funny_stuff = 1
        info.stopCountdown()
    } else {
        game.splash("Try again!", "Hint: Literally do it")
    }
})
let healing_items: Sprite = null
let Enemy_sprite: Sprite = null
let slurp_amount = 0
let projectile: Sprite = null
let player_I_frames = 0
let enemy_damage = 0
let placement = 0
let shield = 0
let Hp = 0
let funny_stuff = 0
let direction = 0
let Player_sprite: Sprite = null
info.startCountdown(180000)
Player_sprite = sprites.create(img`
    ........................
    .....ffff...............
    ...fff22fff.............
    ..fff2222fff............
    .fffeeeeeefff...........
    .ffe222222eef...........
    .fe2ffffff2ef...........
    .ffffeeeeffff...........
    ffefbf44fbfeff..........
    fee41fddf14eef..........
    .ffffdddddeef...........
    fddddf444eef...44.......
    fbbbbf2224d55555544444..
    fbbbbf2224d55555544444..
    .fccf45544d554..........
    ..ffffffff.44...........
    ....ff..ff..............
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    `, SpriteKind.Player)
controller.moveSprite(Player_sprite)
scene.cameraFollowSprite(Player_sprite)
tiles.setCurrentTilemap(tilemap`level0`)
// 0 = right
// 1 = left
direction = 0
tiles.placeOnTile(Player_sprite, tiles.getTileLocation(randint(1, 18), randint(1, 18)))
funny_stuff = 0
Hp = 100
shield = 0
placement = 100
info.setScore(0)
let statusbar = statusbars.create(30, 6, StatusBarKind.Health)
let status_bar_shield = statusbars.create(30, 6, StatusBarKind.Health)
statusbar.setBarBorder(1, 15)
status_bar_shield.setBarBorder(1, 15)
status_bar_shield.setColor(9, 15, 8)
statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
status_bar_shield.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
statusbar.setStatusBarFlag(StatusBarFlag.IgnoreValueEvents, true)
status_bar_shield.setStatusBarFlag(StatusBarFlag.IgnoreValueEvents, true)
statusbar.setStatusBarFlag(StatusBarFlag.HideTargetPreview, true)
status_bar_shield.setStatusBarFlag(StatusBarFlag.HideTargetPreview, true)
statusbar.setStatusBarFlag(StatusBarFlag.LabelAtEnd, true)
status_bar_shield.setStatusBarFlag(StatusBarFlag.LabelAtEnd, true)
if (game.askForString("Do you want a timer (type y for Yes)", 1) == "y") {
    info.startCountdown(game.askForNumber("How long?"))
}
if (game.askForString("Do you want hard mode (type y for Yes)", 1) == "y") {
    enemy_damage = -3
} else {
    enemy_damage = -1
}
player_I_frames = 100
game.setGameOverScoringType(game.ScoringType.HighScore)
game.onUpdateInterval(placement * 10, function () {
    Enemy_sprite = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
    tiles.placeOnTile(Enemy_sprite, tiles.getTileLocation(randint(1, 18), randint(1, 18)))
    Enemy_sprite.follow(Player_sprite, 50)
    Enemy_sprite.lifespan = 100000000000
})
game.onUpdateInterval(6500, function () {
    if (Math.percentChance(10)) {
        healing_items = sprites.create(img`
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
            `, SpriteKind.slurp)
    } else if (Math.percentChance(15)) {
        healing_items = sprites.create(img`
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
            `, SpriteKind.Big_pot)
    } else if (Math.percentChance(25)) {
        healing_items = sprites.create(img`
            . 1 1 2 2 2 1 1 . 
            1 1 1 2 2 2 1 1 1 
            1 1 2 2 1 2 2 1 1 
            1 1 2 1 1 1 2 1 1 
            1 1 2 2 1 2 2 1 1 
            1 1 1 2 2 2 1 1 1 
            . 1 1 2 2 2 1 1 . 
            `, SpriteKind.Medkit)
    } else if (Math.percentChance(40)) {
        healing_items = sprites.create(img`
            . e e . 
            . f f . 
            f 9 9 f 
            f 9 9 f 
            f 9 9 f 
            f 9 9 f 
            . f f . 
            `, SpriteKind.minis)
    } else if (Math.percentChance(55)) {
        healing_items = sprites.create(img`
            . 1 d 1 1 1 1 1 d 1 . 
            1 1 d 1 1 2 1 1 d 1 1 
            1 1 d 1 2 2 2 1 d 1 1 
            1 1 d 1 1 2 1 1 d 1 1 
            . 1 d 1 1 1 1 1 d 1 . 
            `, SpriteKind.bandages)
    }
    tiles.placeOnTile(healing_items, tiles.getTileLocation(randint(1, 18), randint(1, 18)))
})
forever(function () {
    if (player_I_frames > 0) {
        player_I_frames += -1
    }
})
forever(function () {
    if (Hp > 100) {
        Hp = 100
    }
    if (shield > 100) {
        shield = 100
    }
})
forever(function () {
    statusbar.value = Hp
    status_bar_shield.value = shield
    status_bar_shield.setLabel(convertToText(shield), 1)
    if (Hp >= 60) {
        statusbar.setColor(7, 15, 2)
    } else if (Hp >= 40) {
        statusbar.setColor(5, 15, 2)
    } else if (Hp > 20) {
        statusbar.setColor(4, 15, 2)
    } else {
        statusbar.setColor(2, 15, 2)
    }
    if (Hp > 20) {
        statusbar.setLabel(convertToText(Hp), 1)
    } else {
        statusbar.setLabel(convertToText(Hp), 2)
    }
})
forever(function () {
    if (Hp >= 100) {
        statusbar.setPosition(26, 116)
    } else if (Hp >= 10) {
        statusbar.setPosition(23, 116)
    } else {
        statusbar.setPosition(20, 116)
    }
    if (shield >= 100) {
        status_bar_shield.setPosition(26, 109)
    } else if (shield >= 10) {
        status_bar_shield.setPosition(23, 109)
    } else {
        status_bar_shield.setPosition(20, 109)
    }
})
game.onUpdateInterval(100, function () {
    if (slurp_amount > 1 && Hp < 100) {
        Hp += 1
        slurp_amount += -1
    } else if (slurp_amount > 1 && Hp >= 100) {
        shield += 1
        slurp_amount += -1
    }
})
