class QuestionNode:
    def __init__(self, question):
        self.question = question
        self.yes = None
        self.no = None

    def set_yes_node(self, node):
        self.yes = node

    def set_no_node(self, node):
        self.no = node

class GameTree:
    def __init__(self, root):
        self.root = root
        self.current_node = root

    def start(self):
        while self.current_node is not None:
            print(self.current_node.question)
            answer = self.read_input()
            if answer.lower() == "yes":
                self.answer_yes()
            else:
                self.answer_no()

    def answer_yes(self):
        self.current_node = self.current_node.yes

    def answer_no(self):
        self.current_node = self.current_node.no

    @staticmethod
    def read_input():
        return input()


def set_leaf_node(msg):
    msg.set_yes_node(QuestionNode("Wohoo! I guessed it! Try again?"))
    msg.set_no_node(QuestionNode("Oops! Something went wrong! Try again?"))


def main():
    start_game = QuestionNode("Welcome to the game! Think of a design pattern and answer as yes or no. Ready?")
    flexible = QuestionNode("Does it provide the object creation mechanism that enhances the flexibilities of the existing code?")
    single_instance = QuestionNode("Does it ensure you have at most one instance of a class in your application?")
    singleton_pattern = QuestionNode("Is it Singleton Pattern?")
    builder_pattern = QuestionNode("Is it Builder Pattern?")
    decorator_pattern = QuestionNode("Is it Decorator Pattern?")
    adapter_pattern = QuestionNode("Is it Adapter Pattern?")
    communication = QuestionNode("Is it responsible for how one class communicates with others?")
    mechanism = QuestionNode("Does it provide a mechanism to the context to change its behavior?")
    behaviour = QuestionNode("Is changing behaviour built into its scheme?")
    state_pattern = QuestionNode("Is it State Pattern?")
    strategy_pattern = QuestionNode("Is it Strategy Pattern?")
    observer_pattern = QuestionNode("Is it Observer Pattern?")
    command_pattern = QuestionNode("Is it Command Pattern?")
    assemble = QuestionNode("Does it explain how to assemble objects and classes into a larger structure and simplifies the structure by identifying the relationships?")
    notified = QuestionNode("Does it allow a group of objects to be notified when some state changes?")
    attach = QuestionNode("Does it attach additional behavior to an object dynamically at run-time?")
    decorator_pattern = QuestionNode("Is it Decorator Pattern?")
    adapter_pattern = QuestionNode("Is it Adapter Pattern?")
    msg = QuestionNode("Oops! Something went wrong! Try again?")
    end_msg = QuestionNode("End")

    start_game.set_yes_node(flexible)
    start_game.set_no_node(end_msg)

    flexible.set_yes_node(single_instance)
    flexible.set_no_node(communication)

    single_instance.set_yes_node(singleton_pattern)
    single_instance.set_no_node(builder_pattern)

    communication.set_yes_node(mechanism)
    communication.set_no_node(assemble)

    mechanism.set_yes_node(behaviour)
    mechanism.set_no_node(notified)

    notified.set_yes_node(observer_pattern)
    notified.set_no_node(command_pattern)
    behaviour.set_yes_node(state_pattern)
    behaviour.set_no_node(strategy_pattern)

    assemble.set_yes_node(attach)
    assemble.set_no_node(msg)

    attach.set_yes_node(decorator_pattern)
    attach.set_no_node(adapter_pattern)

    set_leaf_node(singleton_pattern)
    set_leaf_node(builder_pattern)
    set_leaf_node(state_pattern)
    set_leaf_node(strategy_pattern)
    set_leaf_node(observer_pattern)
    set_leaf_node(command_pattern)
    set_leaf_node(decorator_pattern)
    set_leaf_node(adapter_pattern)

    game_tree = GameTree(start_game)
    game_tree.start()


if __name__ == "__main__":
    main()