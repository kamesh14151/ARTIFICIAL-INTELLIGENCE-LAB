move(state(middle,onbox,middle,hasnot), grasp,
     state(middle,onbox,middle,has)).

move(state(P,onfloor,P,hasnot), climb,
     state(P,onbox,P,hasnot)).

move(state(P1,onfloor,P1,H), push(P1,P2),
     state(P2,onfloor,P2,H)).

move(state(P,onfloor,P,H), walk(P1,P),
     state(P1,onfloor,P,H)).
