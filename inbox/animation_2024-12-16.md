---
tags:
    - unreal-engine
create date: 2024-12-16
urls:
---

# Animation

`Blend Space` is actually a blueprint which blend all the animations you selected with the choosen variable, for example walking speed.

hold `ctrl + mouse left button` to preview the blended animation in Blend Space

Note: every time you change the blend space, you should update its references in all blueprints, for example I used it in the ABP_MyAnimationBP -> AnimGraph -> StateMachine -> idle/walk/run, if I change the bs **BS_MyBlendSpace**, I need to update the node in the idle/walk/run state, otherwise, it won't work.

`Animation Montage` is a powerful tool to perform complex animation like attack, been attacked, perform skills etc, it usually used with `Laayered blend per bone` noede.

You can store the animation and use it somewhere else in the blueprint bt **caching** the pose.

## Tips

Take a look at the `Motion matching system`, it's a little bit newer.


## Question

1. What's the additive ability of an animation? Note you can set if the animation is additive in the animation
