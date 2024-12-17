---
tags:
    - unreal-engine
create date: 2024-12-15
urls:
---

# Gameplay Framework

## Key classes in Unreal GP Framework

| Name              | Description                                                                                              | Example                 |
|-------------------|----------------------------------------------------------------------------------------------------------|-------------------------|
| Pawn              | Base class for any actor that can be controlled                                                          | player or AI            |
| Character         | A special type of Pawn which represent for vertially-oriented player                                     | Human-like player or AI |
| Controller        | Can posses a pawn to control its actions, can be divided into **player controller** or **AI controller** | N\A                     |
| Player Controller | A special type of Controller, used by human player t ocontrol **Pawns**                                  | N\A                     |
| Game Mode         | One per level, indicate how other classes works in the gp framework, check **World settings**            | rules for the cur level |
| Game Instance     | Manage the info that games or system need to exist throught the duration of the game                     | N\A                     |
| Game State        | Contain all the data to all players in the game, replicated through the network                          | scores table etc        |
| Player State      | Contain data to its associated players                                                                   | health, ammo count etc  |
| HUD               | A base object to disp UI, easy to create UI, but better use **widgets** to a complex ui                  | N\A                     |
| Camera            | Represent how player see the world                                                                       | N\A                     |
| Level Blueprint   | A level-wide global event graph, it's easy to get any references in the level                            | Trigger some door etc   |
| World Settings    | Level specific settings                                                                                  | Change game mode        | 

Note:

- Controller is not necessary to a Pawn
- Camera can be an actor or a component
- You can set the base class for world settings, but it gonna apply to the game globally

**An example game timeline explain the role of the classes mentioned above**:

pics are at 1:04:32 in gp framework video

## Accessing and storing data in the classes


## Practical Example

the example start at 1:10:00
