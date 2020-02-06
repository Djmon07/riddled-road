from sys import exit
import textwrap

class Scene(object):

    def enter(self):
        print("none.")
        exit(1)

class StartScene(Scene):

    def enter(self):

        print("You are out of the city on your first vaction in awhile.")
        print("Yet round fifty miles out you car stars to sputter.")
        print("Darn you should have gotten your car checked out on time.")
        print("What do you do? 1.Road, 2.Forest, 3.CheckEngine ")
        user_input = input('> ')

        if user_input == '1':
            print("You begin your journey down the road!")
            return 'road'

        elif user_input == '2':
            print("You start to wander into the forest, starting to get lost you decide to turn back.")
            print("Realising you don't know how to get back. You get stuck wondering lost in the forest.")
            return 'death'

        elif user_input == '3':
            print("Climbing under the car to see the issue, you notice the read hot engine of your car.")
            print(" The mechanisms holding it in place seem to have rusted. The engine falls onto you crushing you.")
            return 'death'

        else:
            print("You sit around and wait for help. Alas no one comes you starve.")
            return 'death'

class Road(Scene):

    def enter(self):
        print("As you travel back down the road you notice a barn.")
        print("You are feeling tired but unsure of what to do.")
        print("What do you decide? 1.barn 2.road")
        user_input = input('> ')

        if user_input == '1':
            print("You begin to walk towards the barn a warm light welcomes you inside.")
            return 'barn'

        elif user_input == '2':
            print("You begin to travel down the road, as you work your way down you fall asleep")
            print("zzz")
            print("...ZZZ...")
            print("BEEEP!! An on comming car races towards you.")
            print("You wake up in time for the car to swerve into you.")
            return 'death'

        else:
            print("As you are walking down the road the earth shakes, and you fall into a dark pit.")
            return 'death'

class Barn(Scene):

    def enter(self):
        print("The barn is warm inside.")
        print("You decide to stay for the night and rest till morning.")
        print("Time passes and you begin to drift off.")
        print("As you awake you hear the farmer yelling at you to get out or he will shoot.")
        print("What do you do? 1.Walk out with hands rasied 2.Sneak past 3.Run out")
        user_input = input ("> ")

        if user_input == '1':
            print("You walk out with your hands rasied. The farmer told you it was a good choice.")
            print("Then he tell you to run on outta there.")
            print("He said if he hits you with his bullet you can keep it, but if you dont he will give you a prize")
            print("You make a dash for the road, yet you kept the bullet.")
            return 'death'

        elif user_input == '2':
            print("As you are about to sneak out the fround you notice a hole in the corner of the barn.")
            print("You sneak over and crawl through, looping around the angry farmer.")
            print("You can tell he had a few to many as he stumbled around.")
            print("You sneak through the corn feild and back onto the road.")
            return 'path'

        else user_input == '3':
            print("You make a dash out the door in the front directly at the farmer.")
            print("He has a shot gun, but seems to be slow to the draw.")
            print("Running into him he lost his balence allowing you to safly get away.")
            return 'path'

class Path(Scene):

    def enter(self):
        print("As you make you way away from the farm you come back to the brdige you crossed to get out of the city.")
        print("Sadly its a lift bridge, and its out due to mechanical issue.")
        print("also the water seems to be moving faster then normal.")
        print("You see a guy with a boat going down stream.")
        print("What do you do? 1.Get on boat 2.wait for the bridge 3.Try to jump the gap between the bridges.")
        user_input = input('> ')

        if user_input == '1':
            print("You ask the guy to allow you on the boat.")
            print("Explaining what had happened so far, and he agrees.")
            print("You start going down stream trying to make your way acrose the rapids.")
            print("The boat engine roaring, yet not powerful enough.")
            print("You go down steam untill you go over a water fall".)
            return 'death'

        if user_input == '2':
            print("You decide to wait hoping someone would show up and get the bridge working.")
            print("A few hours pass you begin to wonder if this was a good idea")
            print("..........................")
            print("..........................")
            print("...Two hours...")
            print("..........................")
            print("..........................")
            print("Finaly someone comes to the rescue sadly they cannot fix the bridge but,")
            print("They can take you accrost on a cable car".)
            return 'bridge'

        if user_input == '3':
            print("You decide to jump accrost the gap.")
            print("The jump is about elevan feet.")
            print("You get a running head start at the gap.")
            print("Lunging across you grab the edge, but struggle to pull yourself up.")
            print("You grip begins to loosen, as time goes on.")
            print("Luckly a gust of wind pushes from below to give you the boost you need to get over.")
            return 'bridge'

class Bridge(Scene):

    def enter(self):
        print("You made it to the other side finally making your home streach back to the city.")
        return 'finish'

class Death(Scene):

    def enter(self):
        print("You feel your body begin to turn cold. You died!")
        return 'death'
        exit(1)

class Finished(Scene):

    def enter(self):
        print("You made it back to the city!")
        print("The smells of food gets your attention.")
        print("You decide to go get somthing to eat.")
        print("Winner Winner Chicken Dinner.")
        return 'finish'
        exit(1)
