@namespace
class SpriteKind:
    HarmlessZombie = SpriteKind.create()
    Chest = SpriteKind.create()
    HealthPack = SpriteKind.create()
    Boss = SpriteKind.create()
    Key = SpriteKind.create()
    EnemyProjectile = SpriteKind.create()
    Gate = SpriteKind.create()
# gate spawn
def spawnGate():
    global gateAlive, thisGatex, thisGatey1, thisGatey2, gate2
    gateAlive = True
    thisGatex = gatex
    thisGatey1 = gatey1
    thisGatey2 = gatey2
    tiles.set_wall_at(tiles.get_tile_location(thisGatex, thisGatey1), True)
    tiles.set_wall_at(tiles.get_tile_location(thisGatex, thisGatey2), True)
    gate2 = sprites.create(img("""
            dddfdd555ddfdddf
                    dddfdd555ddfdddf
                    dddfff5d5ddfffff
                    dddfdd5d5ddfdddf
                    dddfdd555ddfdddf
                    dddfdd555ddfdddf
                    ffffdd555fffdddf
                    dddfdd5d5ddfdddf
                    dddfdd5d5ddfdddf
                    dddfdd5d5ddfdddf
                    dddfff555ddfffff
                    dddf5555555fdddf
                    ddd555555555dddf
                    ddd555555555dddf
                    fff555555555dddf
                    ddd551115155dddf
                    fdd551111155fddd
                    fdd551115155ffff
                    fdd555555555fddd
                    fdd555555555fddd
                    fdd555555555fddd
                    ffff55555555fddd
                    fdddfd555dddfddd
                    fdddfd5d5dddfddd
                    fdddfd5d5dddfddd
                    fdddff5d5dddffff
                    fdddfd555dddfddd
                    fdddfd555dddfddd
                    fdddfd5d5dddfddd
                    fffffd5d5ffffddd
                    fdddfd5d5dddfddd
                    fdddfd555dddfddd
        """),
        SpriteKind.Gate)
    gate2.set_position(spawnPositionX, spawnPositionY)
    
    def on_on_update():
        global keys, gateAlive
        if abs(fufu.x - gate2.x) <= 20 and abs(fufu.y - gate2.y) <= 20 and keys > 0 and gateAlive == True:
            keys -= 1
            gate2.destroy()
            gateAlive = False
    game.on_update(on_on_update)
    
# sprites & variable setup

def on_on_overlap(sprite, otherSprite):
    sprite.set_kind(SpriteKind.HarmlessZombie)
    otherSprite.start_effect(effects.cool_radial, 600)
    music.wawawawaa.play()
    info.change_life_by(-1)
    sprite.destroy()
sprites.on_overlap(SpriteKind.EnemyProjectile, SpriteKind.player, on_on_overlap)

# player opens chest

def on_on_overlap2(player2, chest):
    global openChest, coinsEarned
    info.change_score_by(50)
    music.ba_ding.play()
    chest.destroy()
    openChest = sprites.create(img("""
            . b b b b b b b b b b b b b b . 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                    b b b b b b b d d b b b b b b b 
                    . b b b b b b c c b b b b b b . 
                    b c c c c c b c c b c c c c c b 
                    b c c c c c c b b c c c c c c b 
                    b c c c c c c c c c c c c c c b 
                    b c c c c c c c c c c c c c c b 
                    b b b b b b b b b b b b b b b b 
                    b e e e e e e e e e e e e e e b 
                    b e e e e e e e e e e e e e e b 
                    b c e e e e e e e e e e e e c b 
                    b b b b b b b b b b b b b b b b 
                    . b b . . . . . . . . . . b b .
        """),
        0)
    openChest.set_position(chest.x, chest.y)
    coinsEarned = sprites.create(img("""
            ................................
                    .....7......f555555..f555555....
                    .....7......f5.......f5....5....
                    .....7......f5.......f5....5....
                    .....7......f5.......f5....5....
                    .....7......f5.......f5....5....
                    .....7......f555555..f5....5....
                    7777777777..ffffff5..f5....5....
                    fffff7...........f5..f5....5....
                    ....f7...........f5..f5....5....
                    ....f7...........f5..f5....5....
                    ....f7...........f5..f5....5....
                    ....f7.....fffffff5..f555555....
                    ....f7.....55555555..fffffff....
                    ................................
                    ................................
        """),
        0)
    coinsEarned.set_position(chest.x, chest.y - 10)
    pause(500)
    coinsEarned.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Chest, on_on_overlap2)

# blaster

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    7 7 1 7 7 7 7 7 7 7 7 1 7 7 1 7 
                    7 7 7 7 1 7 7 7 1 7 7 7 7 7 7 7 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        fufu,
        blasterVelocityX,
        blasterVelocityY)
    music.pew_pew.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# zombie hit

def on_on_overlap3(sprite, otherSprite):
    global maxZombies
    maxZombies += -1
    sprite.destroy()
    otherSprite.destroy()
    otherSprite.start_effect(effects.fire, 300)
    music.thump.play()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap3)

# player gets hp

def on_on_overlap4(player2, hp):
    global hpEarned
    info.change_life_by(2)
    music.ba_ding.play()
    hp.destroy()
    hpEarned = sprites.create(img("""
            ........................................
                    .....7.....2222222.....2f....2f.2222222.
                    .....7.....2fffff2.....2f....2f.2fffff2.
                    .....7.....f....f2.....2f....2f.2f....2.
                    .....7..........f2.....2f....2f.2f....2.
                    .....7..........f2.....2f....2f.2f....2.
                    .....7........fff2.....2f....2f.2f....2.
                    7777777777...ff22......2222222f.2222222.
                    fffff7.....fff22.......2fffff2f.2ffffff.
                    ....f7....ff222........2f....2f.2f......
                    ....f7....f22..........2f....2f.2f......
                    ....f7....f2...........2f....2f.2f......
                    ....f7....f22222222....2f....2f.2f......
                    ....f7....fffffffff....2f....2f.2f......
                    ........................................
                    ........................................
        """),
        0)
    hpEarned.set_position(hp.x, hp.y - 10)
    pause(1000)
    hpEarned.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.HealthPack, on_on_overlap4)

# bossZombie
def spawnBossZombie():
    global bossZombie, thisEnemyMovement2, movementSequence2, enemyAlive2, bossHp, enemyMoveX2, enemyMoveY2, enemyMoveTime2
    bossZombie = sprites.create(img("""
            ................................
                    ..............66........6.......
                    ..............666......666......
                    .............f666ffffff666ff....
                    ............ff7777777777777ff...
                    ............f777f77777777777ff..
                    ............f777fff777777ff7ff..
                    ...........ff77777fff777ff777f..
                    ...........f77771111ff7ff1777f..
                    ..........6f777711111fff11177f..
                    .........66f7777112117711121ff..
                    ...........f7777111117711111f...
                    ..........6f7777111177711117f...
                    .........66f777777777fff7777f...
                    ...........f77777777f77ff77ff...
                    ...........f777777777777777f....
                    ...........f7777777777777fff....
                    ...........f777777777777ff......
                    .........ff7777777777777ff......
                    .......fff777f77f77f77f77f......
                    ......ff77777f77f77f77f77f......
                    .....ff777777f77f77f77f77ff.....
                    ....ff7777777f77f77f77f777f.....
                    ...f77777fff7ffff77ffff777ff....
                    ...f7777ff.f77ff7777ff77777f....
                    ...fffff...f777777777777777f....
                    ...........f777777777777777f....
                    ...........f777777ffff77777f....
                    ...........f777fff...ff7777f....
                    ...........fffff......f7ff7f....
                    ............ff........ffffff....
                    ................................
        """),
        SpriteKind.Boss)
    bossZombie.set_position(spawnPositionX, spawnPositionY)
    thisEnemyMovement2 = enemyMovement
    movementSequence2 = 1
    enemyAlive2 = True
    bossHp = 50
    
    def on_on_destroyed():
        global enemyAlive2
        enemyAlive2 = False
        key: Sprite = sprites.create(img("""
                ................................
                            ...ffffffff.....................
                            ..f5555555f........ffffffffff...
                            .f5.......5f.......f555ff555f...
                            f5.........5f......f555ff555f...
                            f5.........5ffffffff555ff555f...
                            f5.........55555555555555555f...
                            f5.........55555555555555555f...
                            f5.........55555555555555555f...
                            f5.........5fffffffffffffffff...
                            f5.........5f...................
                            .f5.......5f....................
                            ..f5555555f.....................
                            ...fffffff......................
                            ................................
                            ................................
            """),
            SpriteKind.Key)
        key.set_position(bossZombie.x, bossZombie.y)
    bossZombie.on_destroyed(on_on_destroyed)
    
    # enemy movement setup
    if thisEnemyMovement2 == 1:
        enemyMoveX2 = 0
        enemyMoveY2 = 30
        enemyMoveTime2 = 1000
    
    def on_update_interval():
        global movementSequence2, enemyMoveY2
        if thisEnemyMovement2 == 1:
            bossZombie.set_velocity(enemyMoveX2, enemyMoveY2)
            movementSequence2 += 1
            if movementSequence2 > 4:
                movementSequence2 = 1
            if movementSequence2 == 1 or movementSequence2 == 4:
                enemyMoveY2 = 40
            if movementSequence2 == 2 or movementSequence2 == 3:
                enemyMoveY2 = -40
    game.on_update_interval(enemyMoveTime2, on_update_interval)
    
    
    def on_on_update2():
        
        def on_on_overlap5(blast, boss):
            global bossHp
            bossHp = bossHp - 1
            blast.destroy()
            boss.start_effect(effects.fire, 100)
            music.thump.play()
            if bossHp <= 0:
                boss.start_effect(effects.disintegrate, 300)
                boss.destroy()
                music.small_crash.play()
        sprites.on_overlap(SpriteKind.projectile, SpriteKind.Boss, on_on_overlap5)
        
    game.on_update(on_on_update2)
    
    
    def on_update_interval2():
        global bossCooldown
        if enemyAlive2 == True:
            if abs(fufu.x - bossZombie.x) <= 70 and abs(fufu.y - bossZombie.y) <= 70:
                bossCooldown += 1
                if bossCooldown < 19:
                    enemyProjectile = sprites.create_projectile_from_sprite(img("""
                            . . f f f f f f f . . . . . . .
                                                . f 7 7 7 7 7 7 7 f . . . . . .
                                                f 7 7 7 7 7 7 7 7 7 f . . . . .
                                                f 7 6 6 6 7 7 7 7 7 f . . . . .
                                                f 7 6 6 6 7 7 7 7 7 f . . . . .
                                                f 7 6 6 6 7 7 7 7 7 f . . . . .
                                                f 7 7 7 7 7 7 7 7 7 f . . . . .
                                                f 7 7 7 7 7 7 7 6 7 f . . . . .
                                                f 7 7 7 7 6 7 6 7 7 f . . . . .
                                                . f 7 7 7 7 7 7 7 f . . . . . .
                                                . . f f f f f f f . . . . . . .
                                                . . . . . . . . . . . . 7 . . .
                                                . . . . . . . . . 7 . . . . . .
                                                . . . . . . . . . . . . . . . .
                                                . . . . . . . . . . . . 7 . . .
                                                . . . . . . . . . . . . . . . .
                        """),
                        bossZombie,
                        -200,
                        0)
                    enemyProjectile.set_kind(SpriteKind.EnemyProjectile)
                    music.knock.play()
                if bossCooldown > 29:
                    bossCooldown = 0
    game.on_update_interval(100, on_update_interval2)
    
# level setup
def level1SetUp():
    global enemyMovement, spawnPositionX, spawnPositionY, gatex, gatey1, gatey2
    # set scene
    scene.set_background_color(6)
    tiles.set_tilemap(tilemap("""
        level1
    """))
    # zombies1
    enemyMovement = 1
    spawnPositionX = 95
    spawnPositionY = 325
    spawnZombie()
    # zombie2
    enemyMovement = 2
    spawnPositionX = 16
    spawnPositionY = 325
    spawnZombie()
    # zombie3
    enemyMovement = 3
    spawnPositionX = 191
    spawnPositionY = 324
    spawnZombie()
    # zombie4
    spawnPositionX = 16
    spawnPositionY = 490
    spawnZombie()
    # chest1
    spawnPositionX = 80
    spawnPositionY = 416
    spawnChest()
    # hp1
    spawnPositionX = 288
    spawnPositionY = 400
    spawnHealthPack()
    # zombieBoss
    enemyMovement = 1
    spawnPositionX = 592
    spawnPositionY = 384
    spawnBossZombie()
    # spawnGate
    spawnPositionX = 696
    spawnPositionY = 416
    gatex = 43
    gatey1 = 25
    gatey2 = 26
    spawnGate()
    
    def on_update_interval3():
        global spawnPositionX, spawnPositionY, enemyMovement
        if maxZombies < 300:
            spawnPositionX = 240
            spawnPositionY = 80
            spawnPositionX += Math.random_range(-10, 10)
            spawnPositionY += Math.random_range(-10, 10)
            enemyMovement = Math.pick_random([1, 2, 3, 4])
            spawnZombie()
    game.on_update_interval(10000, on_update_interval3)
    
    
    def on_update_interval4():
        global spawnPositionX, spawnPositionY, enemyMovement
        if maxZombies < 300:
            spawnPositionX = 64
            spawnPositionY = 240
            spawnPositionX += Math.random_range(-10, 10)
            spawnPositionY += Math.random_range(-10, 10)
            enemyMovement = Math.pick_random([1, 2, 3, 4])
            spawnZombie()
    game.on_update_interval(10000, on_update_interval4)
    
    
    def on_update_interval5():
        global spawnPositionX, spawnPositionY, enemyMovement
        if maxZombies < 300:
            spawnPositionX = 272
            spawnPositionY = 224
            spawnPositionX += Math.random_range(-10, 10)
            spawnPositionY += Math.random_range(-10, 10)
            enemyMovement = Math.pick_random([1, 3])
            spawnZombie()
    game.on_update_interval(10000, on_update_interval5)
    
    
    def on_update_interval6():
        global spawnPositionX, spawnPositionY, enemyMovement
        if maxZombies < 300:
            spawnPositionX = 560
            spawnPositionY = 224
            spawnPositionX += Math.random_range(-10, 10)
            spawnPositionY += Math.random_range(-10, 10)
            enemyMovement = Math.pick_random([1, 3])
            spawnZombie()
    game.on_update_interval(10000, on_update_interval6)
    
    
    def on_update_interval7():
        global spawnPositionX, spawnPositionY, enemyMovement
        if maxZombies < 300:
            spawnPositionX = 336
            spawnPositionY = 304
            spawnPositionX += Math.random_range(-10, 10)
            spawnPositionY += Math.random_range(-10, 10)
            enemyMovement = Math.pick_random([1, 3])
            spawnZombie()
    game.on_update_interval(10000, on_update_interval7)
    
    
    def on_update_interval8():
        global spawnPositionX, spawnPositionY, enemyMovement
        if maxZombies < 300:
            spawnPositionX = 272
            spawnPositionY = 400
            spawnPositionX += Math.random_range(-10, 10)
            spawnPositionY += Math.random_range(-10, 10)
            enemyMovement = Math.pick_random([1, 3])
            spawnZombie()
    game.on_update_interval(10000, on_update_interval8)
    
# player hit

def on_on_overlap6(sprite, otherSprite):
    sprite.set_kind(SpriteKind.HarmlessZombie)
    otherSprite.start_effect(effects.cool_radial, 600)
    music.wawawawaa.play()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap6)

# chest spawn
def spawnChest():
    global chest
    chest = sprites.create(img("""
            . . b b b b b b b b b b b b . . 
                    . b e 4 4 4 4 4 4 4 4 4 4 e b . 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                    b e e e e e e e e e e e e e e b 
                    b e e e e e e e e e e e e e e b 
                    b b b b b b b d d b b b b b b b 
                    c b b b b b b c c b b b b b b c 
                    c c c c c c b c c b c c c c c c 
                    b e e e e e c b b c e e e e e b 
                    b e e e e e e e e e e e e e e b 
                    b c e e e e e e e e e e e e c b 
                    b b b b b b b b b b b b b b b b 
                    . b b . . . . . . . . . . b b .
        """),
        SpriteKind.Chest)
    chest.set_position(spawnPositionX, spawnPositionY)

def on_on_overlap7(sprite, otherSprite):
    pause(500)
    sprite.set_kind(SpriteKind.enemy)
sprites.on_overlap(SpriteKind.HarmlessZombie, SpriteKind.player, on_on_overlap7)

# player gets key

def on_on_overlap8(player2, key):
    global keys
    key.destroy()
    music.ba_ding.play()
    keys += 1
    player.say("Key Obtained", 1000, 7, 15)
sprites.on_overlap(SpriteKind.player, SpriteKind.Key, on_on_overlap8)

# spawnFunctions
# zombie
def spawnZombie():
    global maxZombies, zombies, thisEnemyMovement, movementSequence, enemyAlive, enemyMoveX, enemyMoveY, enemyMoveTime
    maxZombies += 1
    zombies = sprites.create(assets.image("""
        zombie
    """), SpriteKind.enemy)
    zombies.set_position(spawnPositionX, spawnPositionY)
    thisEnemyMovement = enemyMovement
    movementSequence = 1
    enemyAlive = True
    # enemy movement setup
    if thisEnemyMovement == 1:
        enemyMoveX = 20
        enemyMoveY = 0
        enemyMoveTime = 4000
    if thisEnemyMovement == 2:
        enemyMoveX = -20
        enemyMoveY = 0
        enemyMoveTime = 4000
    if thisEnemyMovement == 3:
        enemyMoveX = 20
        enemyMoveY = 0
        movementSequence = 2
        enemyMoveTime = 9000
    if thisEnemyMovement == 4:
        enemyMoveX = 20
        enemyMoveY = 0
        movementSequence = 4
        enemyMoveTime = 9000
    
    def on_update_interval9():
        global enemyMoveX, movementSequence
        if thisEnemyMovement == 1 or thisEnemyMovement == 2:
            zombies.set_velocity(enemyMoveX, enemyMoveY)
            enemyMoveX = enemyMoveX * -1
        if thisEnemyMovement == 3 or thisEnemyMovement == 4:
            if movementSequence == 4:
                zombies.set_velocity(0, -20)
                movementSequence += 1
            if movementSequence == 3:
                zombies.set_velocity(-20, 0)
                movementSequence += 1
            if movementSequence == 2:
                zombies.set_velocity(0, 20)
                movementSequence += 1
            if movementSequence == 1:
                zombies.set_velocity(20, 0)
                movementSequence += 1
            if movementSequence > 4:
                movementSequence = 1
    game.on_update_interval(enemyMoveTime, on_update_interval9)
    
# healthpack spawn
def spawnHealthPack():
    global healthPack
    healthPack = sprites.create(img("""
            . f f f f f f f f f f f f f f f 
                    . f 1 1 1 1 1 1 1 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 1 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 2 2 2 2 2 2 2 2 2 2 2 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 2 1 1 1 1 1 1 f 
                    . f 1 1 1 1 1 1 1 1 1 1 1 1 1 f 
                    . f f f f f f f f f f f f f f f
        """),
        SpriteKind.HealthPack)
    healthPack.set_position(spawnPositionX, spawnPositionY)
healthPack: Sprite = None
enemyAlive = False
chest: Sprite = None
hpEarned: Sprite = None
blasterVelocityX = 0
projectile: Sprite = None
coinsEarned: Sprite = None
openChest: Sprite = None
gate2: Sprite = None
gatey2 = 0
thisGatey2 = 0
gatey1 = 0
thisGatey1 = 0
gatex = 0
thisGatex = 0
gateAlive = False
blasterVelocityY = 0
keys = 0
enemyMoveX = 0
enemyMoveY = 0
enemyMoveTime = 0
enemyMoveX2 = 0
enemyMoveY2 = 0
enemyMoveTime2 = 0
bossCooldown = 0
gate = None
fufu: Sprite = None
spawnPositionX = 0
spawnPositionY = 0
enemyMovement = 0
maxZombies = 0
bossZombie: Sprite = None
thisEnemyMovement2 = 0
movementSequence2 = 0
enemyAlive2 = False
bossHp = 0
zombies: Sprite = None
thisEnemyMovement = 0
movementSequence = 0
blasterVelocityY = 200
info.set_life(10)
info.set_background_color(15)
info.set_font_color(2)
info.set_border_color(7)
# controls setup
fufu = sprites.create(img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ....fffff........fffff..........
            ....fffff11111111fffff..........
            .7...ffff11111111ffff.....7.....
            .17...11111111111111.....77.....
            .77....111ff11ff111......71.....
            .71....111bf11fb111......77.....
            .77....11111331111.......71.....
            .77.....1111131111.......77.....
            .17......11cccc11........17.....
            .77......fffffffff.......77.....
            .77.....fffffffffff......71.....
            .71.....fff11111ffff.....77.....
            .77.1fffff1111111ffffff1.77.....
            .777ffffff11111111ffffff117.....
            .7771fffff1111111ffffff1777.....
            .......ffff111111ffff...........
            .........fffffffffff............
            ..........ffffffff..............
            ..........fff..fff..............
            ..........fff..fff..............
            ..........ff....ff..............
            ................................
            ................................
            ................................
    """),
    SpriteKind.player)
controller.move_sprite(fufu)
scene.camera_follow_sprite(fufu)
# run game
level1SetUp()
# aiming

def on_on_update3():
    global blasterVelocityY, blasterVelocityX
    # up
    if controller.up.is_pressed():
        blasterVelocityY = -200
        blasterVelocityX = 0
        # angles
        if controller.right.is_pressed():
            blasterVelocityX = 200
        if controller.left.is_pressed():
            blasterVelocityX = -200
    # down
    if controller.down.is_pressed():
        blasterVelocityY = 200
        blasterVelocityX = 0
        # angles
        if controller.right.is_pressed():
            blasterVelocityX = 200
        if controller.left.is_pressed():
            blasterVelocityX = -200
    # left
    if controller.left.is_pressed():
        blasterVelocityY = 0
        blasterVelocityX = -200
        # angles
        if controller.up.is_pressed():
            blasterVelocityY = -200
        if controller.down.is_pressed():
            blasterVelocityY = 200
    if controller.right.is_pressed():
        blasterVelocityY = 0
        blasterVelocityX = 200
        # angles
        if controller.up.is_pressed():
            blasterVelocityY = -200
        if controller.down.is_pressed():
            blasterVelocityY = 200
game.on_update(on_on_update3)
