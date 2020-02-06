from sys import exit
import textwrap

class StartScene(object):

    def enter(self):

        print(dedent("""
            You are out of the city on your first vaction in awhile.
            Yet round fifty miles out you car stars to sputter.
            Darn you should have gotten your car checked out on time.
            What do you do? 1.Road, 2.Forest, 3.CheckEngine """))
        user_input = input('> ')

        if user_input == '1':
            print("You begin your journey down the road!")
            return 'road'

        elif user_input == '2':
            print(dedent("""
                You start to wander into the forest, starting to get lost you decide to turn back.
                Realising you don't know how to get back. You get stuck wondering lost in the forest.""")
            return 'death'

        elif user_input == '3':
            print(dedent("""
                Climbing under the car to see the issue, you notice the read hot engine of your car.
                The mechanisms holding it in place seem to have rusted.
                The engine falls onto you crushing you."""))
            return 'death'

        else:
            print("You sit around and wait for help. Alas no one comes you starve.")
            return 'death'

class Road(object):

    def enter(self):
        print(dedent("""
            As you travel back down the road you notice a barn.
            You are feeling tired but unsure of what to do.
            What do you decide? 1.barn 2.road"""))
        user_input = input('> ')

        if user_input == '1':
            print("You begin to walk towards the barn a warm light welcomes you inside.")
            return 'barn'

        elif user_input == '2':
            print(dedent("""
                You begin to travel down the road, as you work your way down you fall asleep
                zzz
                ...ZZZ...
                BEEEP!! An on comming car races towards you.
                You wake up in time for the car to swerve into you."""))
            return 'death'

        else:
            print("As you are walking down the road the earth shakes, and you fall into a dark pit.")
            return 'death'

class Barn(object):

    def enter(self):
        print(dedent("""
            The barn is warm inside.
            You decide to stay for the night and rest till morning.
            Time passes and you begin to drift off.
            As you awake you hear the farmer yelling at you to get out or he will shoot.
            What do you do? 1.Walk out with hands rasied 2.Sneak past 3.Run out"""))
        user_input = input ("> ")

        if user_input == '1':
            print(dedent("""
                You walk out with your hands rasied. The farmer told you it was a good choice.
                Then he tell you to run on outta there.
                He said if he hits you with his bullet you can keep it,
                but if you dont he will give you a prize
                You make a dash for the road, yet you kept the bullet."""))
            return 'death'

        elif user_input == '2':
            print(dedent("""
                As you are about to sneak out the fround you notice a hole in the corner of the barn.
                You sneak over and crawl through, looping around the angry farmer.
                You can tell he had a few to many as he stumbled around.
                You sneak through the corn feild and back onto the road."""))
            return 'path'

        elif user_input == '3':
            print(dedent("""
                You make a dash out the door in the front directly at the farmer.
                He has a shot gun, but seems to be slow to the draw.
                Running into him he lost his balence allowing you to safly get away."""))
            return 'path'

        else:
            print("You cluck like a chicken, yet the farmer is not fooled. BANG!!")
            return 'death'

class Path(object):

    def enter(self):
        print(dedent"""
            As you make you way away from the farm you come back to the bridge
            you crossed to get out of the city.
            Sadly its a lift bridge, and its out due to mechanical issue.
            also the water seems to be moving faster then normal.
            You see a guy with a boat going down stream.
            What do you do? 1.Get on boat 2.wait for the bridge 3.
            Try to jump the gap between the bridges."""))
        user_input = input('> ')

        if user_input == '1':
            print(dedent("""
                You ask the guy to allow you on the boat.
                Explaining what had happened so far, and he agrees.
                You start going down stream trying to make your way acrose the rapids.
                The boat engine roaring, yet not powerful enough.
                You go down steam untill you go over a water fall."""))
            return 'death'

        elif user_input == '2':
            print(dedent("""
                You decide to wait hoping someone would show up and get the bridge working.
                A few hours pass you begin to wonder if this was a good idea
                ..........................
                ...Two hours...
                ..........................
                Finaly someone comes to the rescue sadly they cannot fix the bridge but,
                They can take you acrost on a cable car."""))
            return 'bridge'

        elif user_input == '3':
            print(dedent("""
                You decide to jump accrost the gap.
                The jump is about elevan feet.
                You get a running head start at the gap.
                Lunging across you grab the edge, but struggle to pull yourself up.
                You grip begins to loosen, as time goes on.
                Luckly a gust of wind pushes from below to give you the boost you need to get up"""))
            return 'bridge'

        else:
            print("You decide to just jump into the water for a swim.")
            return 'dealth'

class Bridge(object):

    def enter(self):
        print("You made it to the other side finally making your home streach back to the city.")
        return 'finished'

class Death(object):

    def enter(self):
        print("You feel your body begin to turn cold. You died!")
        exit(1)

class Finished(object):

    def enter(self):
        print(dedent("""
            You made it back to the city!
            The smells of food gets your attention.
            You decide to go get somthing to eat.
            Winner Winner Chicken Dinner."""))
        return 'finish'
        exit(1)
