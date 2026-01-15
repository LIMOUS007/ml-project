import random
from engine.task import generate_arithmetic_progression
from engine.task import generate_boolean_evaluation
from engine.task import generate_comparison
from engine.task import generate_constraint_task
from engine.task import generate_cycle_pattern
from engine.task import generate_implication_chain
from engine.task import generate_inverse_ratio_scaling
from engine.task import generate_mental_division
from engine.task import generate_mixed_pattern
from engine.task import generate_multiplicative_progression
from engine.task import generate_near_boundary_task
from engine.task import generate_ratio_scaling
from engine.task import generate_square_task
SKILLS = {
    "numerical": [
        generate_mental_division,
        generate_ratio_scaling,
        generate_inverse_ratio_scaling,
        generate_square_task,
        generate_near_boundary_task
    ],
    "logical": [
        generate_comparison,
        generate_boolean_evaluation,
        generate_implication_chain,
        generate_constraint_task
    ],
    "pattern": [
        generate_arithmetic_progression,
        generate_multiplicative_progression,
        generate_cycle_pattern,
        generate_mixed_pattern
    ]
}

def pick_task(user_state):
    skill = random.choice(list(SKILLS.keys()))
    generator = random.choice(SKILLS[skill])
    return generator(user_state["difficulty"])
