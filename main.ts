namespace SpriteKind {
    export const HarmlessZombie = SpriteKind.create()
    export const Chest = SpriteKind.create()
    export const HealthPack = SpriteKind.create()
    export const Boss = SpriteKind.create()
    export const Key = SpriteKind.create()
    export const EnemyProjectile = SpriteKind.create()
    export const Gate = SpriteKind.create()
}
// gate spawn
function spawnGate () {
    gateAlive = true
    thisGatex = gatex
    thisGatey1 = gatey1
    thisGatey2 = gatey2
    tiles.setWallAt(tiles.getTileLocation(thisGatex, thisGatey1), true)
    tiles.setWallAt(tiles.getTileLocation(thisGatex, thisGatey2), true)
    gate2 = sprites.create(img`
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
        `, SpriteKind.Gate)
    gate2.setPosition(spawnPositionX, spawnPositionY)
    game.onUpdate(function (){
        if(Math.abs(fufu.x - gate2.x) <= 20 && Math.abs(fufu.y - gate2.y) <= 20
        && keys > 0 && gateAlive == true ){
            keys--
            gate2.destroy()
            gateAlive = false

        } 
    })
}
// sprites & variable setup
sprites.onOverlap(SpriteKind.EnemyProjectile, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.setKind(SpriteKind.HarmlessZombie)
    otherSprite.startEffect(effects.coolRadial, 600)
    music.wawawawaa.play()
    info.changeLifeBy(-1)
    sprite.destroy()
})
// player opens chest
sprites.onOverlap(SpriteKind.Player, SpriteKind.Chest, function (player2, chest) {
    info.changeScoreBy(50)
    music.baDing.play()
    chest.destroy()
    openChest = sprites.create(img`
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
        `, 0)
    openChest.setPosition(chest.x, chest.y)
    coinsEarned = sprites.create(img`
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
        `, 0)
    coinsEarned.setPosition(chest.x, chest.y - 10)
    pause(500)
    coinsEarned.destroy()
})
// blaster
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, fufu, blasterVelocityX, blasterVelocityY)
    music.pewPew.play()
})
// zombie hit
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    maxZombies += -1
    sprite.destroy()
    otherSprite.destroy()
    otherSprite.startEffect(effects.fire, 300)
    music.thump.play()
})
// player gets hp
sprites.onOverlap(SpriteKind.Player, SpriteKind.HealthPack, function (player2, hp) {
    info.changeLifeBy(2)
    music.baDing.play()
    hp.destroy()
    hpEarned = sprites.create(img`
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
        `, 0)
    hpEarned.setPosition(hp.x, hp.y - 10)
    pause(1000)
    hpEarned.destroy()
})
// bossZombie
function spawnBossZombie () {
    bossZombie = sprites.create(img`
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
        `, SpriteKind.Boss)
    bossZombie.setPosition(spawnPositionX, spawnPositionY)
    thisEnemyMovement2 = enemyMovement
    movementSequence2 = 1
    enemyAlive2 = true
    bossHp = 50
    bossZombie.onDestroyed(function(){
        enemyAlive2 = false
        let key: Sprite = sprites.create(img`
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
        `, SpriteKind.Key)
        key.setPosition(bossZombie.x, bossZombie.y)
    })
// enemy movement setup
    if (thisEnemyMovement2 == 1) {
        enemyMoveX2 = 0
        enemyMoveY2 = 30
        enemyMoveTime2 = 1000
    }
    game.onUpdateInterval(enemyMoveTime2, function(){
        if(thisEnemyMovement2 == 1){
            bossZombie.setVelocity(enemyMoveX2, enemyMoveY2)
            movementSequence2++
            if(movementSequence2 > 4){
                movementSequence2 = 1
            }
            if(movementSequence2 == 1 || movementSequence2 == 4){
              enemyMoveY2 = 40     
            }
            if(movementSequence2 == 2 || movementSequence2 == 3){
              enemyMoveY2 = -40     
            }
        }
    })
game.onUpdate(function () {
        sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Boss, 
        function (blast : Sprite, boss : Sprite){
            bossHp = bossHp - 1
            blast.destroy()
            boss.startEffect(effects.fire, 100)
            music.thump.play()
            if(bossHp <= 0){
                boss.startEffect(effects.disintegrate, 300)
                boss.destroy()
                music.smallCrash.play()
            }
        })
    })
game.onUpdateInterval(100, function () {
        if(enemyAlive2 == true){
            if(Math.abs(fufu.x - bossZombie.x) <= 70
            && Math.abs(fufu.y - bossZombie.y) <= 70){
                bossCooldown++
                if(bossCooldown < 19){
                let enemyProjectile = sprites.createProjectileFromSprite(img`
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
                `, 
                    bossZombie, -200, 0)
                    enemyProjectile.setKind(SpriteKind.EnemyProjectile)
                    music.knock.play()
                }

                if(bossCooldown > 29 ){
                    bossCooldown = 0
                }
            }
        }
    })
}
// level setup
function level1SetUp () {
    // set scene
    scene.setBackgroundColor(6)
    tiles.setTilemap(tilemap`level1`)
    // zombies1
    enemyMovement = 1
    spawnPositionX = 95
    spawnPositionY = 325
    spawnZombie()
    // zombie2
    enemyMovement = 2
    spawnPositionX = 16
    spawnPositionY = 325
    spawnZombie()
    // zombie3
    enemyMovement = 3
    spawnPositionX = 191
    spawnPositionY = 324
    spawnZombie()
    // zombie4
    spawnPositionX = 16
    spawnPositionY = 490
    spawnZombie()
    // chest1
    spawnPositionX = 80
    spawnPositionY = 416
    spawnChest()
    // hp1
    spawnPositionX = 288
    spawnPositionY = 400
    spawnHealthPack()
    // zombieBoss
    enemyMovement = 1
    spawnPositionX = 592
    spawnPositionY = 384
    spawnBossZombie()
    // spawnGate
    spawnPositionX = 696
    spawnPositionY = 416
    gatex = 43
    gatey1 = 25
    gatey2 = 26
    spawnGate()
    game.onUpdateInterval(10000, function() {
        if(maxZombies < 300) {
            spawnPositionX = 240
            spawnPositionY = 80
            spawnPositionX += Math.randomRange(-10, 10)
            spawnPositionY += Math.randomRange(-10, 10)
            enemyMovement = Math.pickRandom([1, 2, 3, 4])
            spawnZombie()
        }
    })
game.onUpdateInterval(10000, function() {
        if(maxZombies < 300) {
            spawnPositionX = 64
            spawnPositionY = 240
            spawnPositionX += Math.randomRange(-10, 10)
            spawnPositionY += Math.randomRange(-10, 10)
            enemyMovement = Math.pickRandom([1, 2, 3, 4])
            spawnZombie()
        }
    })
game.onUpdateInterval(10000, function() {
        if(maxZombies < 300) {
            spawnPositionX = 272
            spawnPositionY = 224
            spawnPositionX += Math.randomRange(-10, 10)
            spawnPositionY += Math.randomRange(-10, 10)
            enemyMovement = Math.pickRandom([1, 3])
            spawnZombie()
        }
    })
game.onUpdateInterval(10000, function() {
        if(maxZombies < 300) {
            spawnPositionX = 560
            spawnPositionY = 224
            spawnPositionX += Math.randomRange(-10, 10)
            spawnPositionY += Math.randomRange(-10, 10)
            enemyMovement = Math.pickRandom([1, 3])
            spawnZombie()
        }
    })
game.onUpdateInterval(10000, function() {
        if(maxZombies < 300) {
            spawnPositionX = 336 
            spawnPositionY = 304
             spawnPositionX += Math.randomRange(-10, 10)
            spawnPositionY += Math.randomRange(-10, 10)
            enemyMovement = Math.pickRandom([1, 3])
            spawnZombie()
        }
    })
game.onUpdateInterval(10000, function() {
        if(maxZombies < 300) {
            spawnPositionX =  272
            spawnPositionY = 400
            spawnPositionX += Math.randomRange(-10, 10)
            spawnPositionY += Math.randomRange(-10, 10)
            enemyMovement = Math.pickRandom([1, 3])
            spawnZombie()
        }
    })
}
// player hit
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.setKind(SpriteKind.HarmlessZombie)
    otherSprite.startEffect(effects.coolRadial, 600)
    music.wawawawaa.play()
    info.changeLifeBy(-1)
})
// chest spawn
function spawnChest () {
    chest = sprites.create(img`
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
        `, SpriteKind.Chest)
    chest.setPosition(spawnPositionX, spawnPositionY)
}
sprites.onOverlap(SpriteKind.HarmlessZombie, SpriteKind.Player, function (sprite, otherSprite) {
    pause(500)
    sprite.setKind(SpriteKind.Enemy)
})
// player gets key
sprites.onOverlap(SpriteKind.Player, SpriteKind.Key, function (player2, key) {
    key.destroy()
    music.baDing.play()
    keys += 1
    player.say("Key Obtained", 1000, 7, 15)
})
// spawnFunctions
// zombie
function spawnZombie () {
    maxZombies += 1
    zombies = sprites.create(assets.image`zombie`, SpriteKind.Enemy)
    zombies.setPosition(spawnPositionX, spawnPositionY)
    thisEnemyMovement = enemyMovement
    movementSequence = 1
    enemyAlive = true
    // enemy movement setup
    if (thisEnemyMovement == 1) {
        enemyMoveX = 20
        enemyMoveY = 0
        enemyMoveTime = 4000
    }
    if (thisEnemyMovement == 2) {
        enemyMoveX = -20
        enemyMoveY = 0
        enemyMoveTime = 4000
    }
    if (thisEnemyMovement == 3) {
        enemyMoveX = 20
        enemyMoveY = 0
        movementSequence = 2
        enemyMoveTime = 9000
    }
    if (thisEnemyMovement == 4) {
        enemyMoveX = 20
        enemyMoveY = 0
        movementSequence = 4
        enemyMoveTime = 9000
    }
    game.onUpdateInterval(enemyMoveTime, function(){
        if(thisEnemyMovement == 1 || thisEnemyMovement == 2){
                zombies.setVelocity(enemyMoveX, enemyMoveY)
                enemyMoveX = enemyMoveX * -1
        }
        if(thisEnemyMovement == 3 || thisEnemyMovement == 4){
            if(movementSequence == 4){
                zombies.setVelocity(0, -20)
                movementSequence++
            }
            if(movementSequence == 3){
                zombies.setVelocity(-20, 0)
                movementSequence++

        }
  if(movementSequence == 2){
                zombies.setVelocity(0, 20)
                movementSequence++
            
        }
         if(movementSequence == 1){
                zombies.setVelocity(20, 0)
                movementSequence++  
            }
        if (movementSequence > 4){
            movementSequence = 1
        }
        }
    })
}
// healthpack spawn
function spawnHealthPack () {
    healthPack = sprites.create(img`
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
        `, SpriteKind.HealthPack)
    healthPack.setPosition(spawnPositionX, spawnPositionY)
}
let healthPack: Sprite = null
let enemyAlive = false
let chest: Sprite = null
let hpEarned: Sprite = null
let blasterVelocityX = 0
let projectile: Sprite = null
let coinsEarned: Sprite = null
let openChest: Sprite = null
let gate2: Sprite = null
let gatey2 = 0
let thisGatey2 = 0
let gatey1 = 0
let thisGatey1 = 0
let gatex = 0
let thisGatex = 0
let gateAlive = false
let blasterVelocityY = 0
let keys = 0
let enemyMoveX = 0
let enemyMoveY = 0
let enemyMoveTime = 0
let enemyMoveX2 = 0
let enemyMoveY2 = 0
let enemyMoveTime2 = 0
let bossCooldown = 0
let gate = null
let fufu: Sprite = null
let spawnPositionX = 0
let spawnPositionY = 0
let enemyMovement = 0
let maxZombies = 0
let bossZombie: Sprite = null
let thisEnemyMovement2 = 0
let movementSequence2 = 0
let enemyAlive2 = false
let bossHp = 0
let zombies: Sprite = null
let thisEnemyMovement = 0
let movementSequence = 0
blasterVelocityY = 200
info.setLife(10)
info.setBackgroundColor(15)
info.setFontColor(2)
info.setBorderColor(7)
// controls setup
fufu = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(fufu)
scene.cameraFollowSprite(fufu)
// run game
level1SetUp()
// aiming
game.onUpdate(function () {
    // up
    if (controller.up.isPressed()) {
        blasterVelocityY = -200
        blasterVelocityX = 0
        // angles
        if (controller.right.isPressed()) {
            blasterVelocityX = 200
        }
        if (controller.left.isPressed()) {
            blasterVelocityX = -200
        }
    }
    // down
    if (controller.down.isPressed()) {
        blasterVelocityY = 200
        blasterVelocityX = 0
        // angles
        if (controller.right.isPressed()) {
            blasterVelocityX = 200
        }
        if (controller.left.isPressed()) {
            blasterVelocityX = -200
        }
    }
    // left
    if (controller.left.isPressed()) {
        blasterVelocityY = 0
        blasterVelocityX = -200
        // angles
        if (controller.up.isPressed()) {
            blasterVelocityY = -200
        }
        if (controller.down.isPressed()) {
            blasterVelocityY = 200
        }
    }
    if (controller.right.isPressed()) {
        blasterVelocityY = 0
        blasterVelocityX = 200
        // angles
        if (controller.up.isPressed()) {
            blasterVelocityY = -200
        }
        if (controller.down.isPressed()) {
            blasterVelocityY = 200
        }
    }
})
