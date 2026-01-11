import random
import string
from collections import defaultdict, deque

RELATIONS = [
    "taller than",
    "older than",
    "faster than",
    "heavier than",
    "larger than"
]

REL_WORDS = [
    ("left of", "right of"),
    ("above", "below"),
    ("faster than", "slower than")
]

def comparison_params_from_difficulty(log_difficulty):
    if log_difficulty < 5:
        return 3
    elif log_difficulty < 10:
        return random.randint(4, 5)
    elif log_difficulty < 15:
        return random.randint(6, 7)
    elif log_difficulty < 20:
        return random.randint(8, 11)
    elif log_difficulty < 25:
        return random.randint(12, 15)
    else:
        return random.randint(16, 25)

def boolean_params_from_difficulty(log_difficulty):
    if log_difficulty < 5:
        var_count = 2
        ops_count = 1
        allow_not = False
    elif log_difficulty < 10:
        var_count = random.choice([2, 3])
        ops_count = 2
        allow_not = False
    elif log_difficulty < 15:
        var_count = 3
        ops_count = 2
        allow_not = True
    elif log_difficulty < 20:
        var_count = random.choice([3, 4])
        ops_count = random.choice([2, 3])
        allow_not = True
    elif log_difficulty < 25:
        var_count = random.choice([4, 5])
        ops_count = random.choice([3, 4])
        allow_not = True
    else:
        var_count = random.choice([4, 6])
        ops_count = random.choice([3, 5])
        allow_not = True
    return var_count, ops_count, allow_not

def implication_params_from_difficulty(log_difficulty):
    if log_difficulty < 5:
        vars_count = 3
        edges = 2
    elif log_difficulty < 10:
        vars_count = 4
        edges = 3
    elif log_difficulty < 15:
        vars_count = random.choice([4, 5])
        edges = random.choice([3, 4])
    elif log_difficulty < 20:
        vars_count = random.choice([5, 6])
        edges = random.choice([4, 5])
    elif log_difficulty < 25:
        vars_count = random.choice([6, 7])
        edges = random.choice([5, 6])
    else:
        vars_count = random.choice([7, 8, 9])
        edges = random.choice([6, 7, 8])
    return vars_count, edges

def constraint_params_from_difficulty(log_difficulty):
    if log_difficulty < 5:
        n_objects = 3
        n_constraints = 2
    elif log_difficulty < 10:
        n_objects = 4
        n_constraints = 3
    elif log_difficulty < 15:
        n_objects = random.choice([4, 5])
        n_constraints = random.choice([3, 4])
    elif log_difficulty < 20:
        n_objects = random.choice([5, 6])
        n_constraints = random.choice([4, 5])
    elif log_difficulty < 25:
        n_objects = random.choice([6, 7])
        n_constraints = random.choice([5, 6])
    else:
        n_objects = random.choice([7, 8, 9])
        n_constraints = random.choice([6, 7, 8])
    return n_objects, n_constraints

def ap_params_from_difficulty(pat_difficulty):
    if pat_difficulty < 5:
        length = 4
        step_max = 5
    elif pat_difficulty < 10:
        length = 5
        step_max = 7
    elif pat_difficulty < 15:
        length = random.choice([5, 6])
        step_max = 10
    elif pat_difficulty < 20:
        length = random.choice([6, 7])
        step_max = 15
    elif pat_difficulty < 25:
        length = random.choice([7, 8])
        step_max = random.choice([15, 20])
    else:
        length = random.choice([9, 10, 11, 12, 13])
        step_max = random.choice([25, 30, 35])
    return length, step_max

def mp_params_from_difficulty(pat_difficulty):
    if pat_difficulty < 5:
        length = 4
        multipliers = [2]
        start = random.randint(1, 5)
    elif pat_difficulty < 10:
        length = 5
        multipliers = [2]
        start = random.randint(1, 10)
    elif pat_difficulty < 15:
        length = random.choice([5, 6])
        multipliers = [2, 3]
        start = random.randint(1, 15)
    elif pat_difficulty < 20:
        length = 6
        multipliers = [2, 3]
        start = random.randint(1, 20)
    elif pat_difficulty < 25:
        length = random.choice([6, 7])
        multipliers = [2, 3, 4]
        start = random.randint(1, 25)
    else:
        length = random.choice([7, 8, 9])
        multipliers = [3, 4, 5]
        start = random.randint(10, 30)
    return length, multipliers, start

def cycle_params_from_difficulty(pat_difficulty):
    if pat_difficulty < 5:
        cycle_len = 2
        total_len = random.randint(4, 5)
    elif pat_difficulty < 10:
        cycle_len = 3
        total_len = random.randint(6, 7)
    elif pat_difficulty < 15:
        cycle_len = random.choice([3, 4])
        total_len = random.randint(7, 9)
    elif pat_difficulty < 20:
        cycle_len = random.choice([4, 5])
        total_len = random.randint(8, 11)
    elif pat_difficulty < 25:
        cycle_len = random.choice([5, 6])
        total_len = random.randint(10, 13)
    else:
        cycle_len = random.choice([6, 7, 8])
        total_len = random.randint(12, 20)
    return cycle_len, total_len

def mixed_params_from_difficulty(pat_difficulty):
    if pat_difficulty < 5:
        op_len = 2
        seq_len = random.randint(4, 5)
        k_max = 3
    elif pat_difficulty < 10:
        op_len = 2
        seq_len = random.randint(5, 6)
        k_max = 5
    elif pat_difficulty < 15:
        op_len = random.choice([2, 3])
        seq_len = random.randint(6, 7)
        k_max = 6
    elif pat_difficulty < 20:
        op_len = random.choice([2, 3])
        seq_len = random.randint(7, 8)
        k_max = 8
    elif pat_difficulty < 25:
        op_len = random.choice([2, 4])
        seq_len = random.randint(8, 10)
        k_max = 10
    else:
        op_len = random.choice([3, 4])
        seq_len = random.randint(10, 15)
        k_max = 12
    return op_len, seq_len, k_max

def division_params_from_difficulty(num_diff):
    if num_diff < 5:
        base = random.choice([2, 3, 5])
        return base
    elif num_diff < 10:
        base = random.choice([2, 3, 5])
        power = random.choice([2, 3])
        return base * power
    elif num_diff < 15:
        base = random.choice([2, 3, 5])
        power = random.choice([2, 3, 5])
        return base * power
    elif num_diff < 20:
        base = random.choice([2, 3, 5])
        power = random.choice([4, 5, 8 , 9])
        return base * power
    elif num_diff < 25:
        base = random.choice([2, 3, 5])
        power = random.choice([4, 5, 8 , 9])
        return base * power
    else:
        base = random.choice([2, 3, 5])
        power = random.choice([2, 3, 4, 5, 8, 9])
        return base * power
    
def ratio_params_from_difficulty(num_diff):
    if num_diff < 5:
        k = random.randint(2, 3)
    elif num_diff < 10:
        k = random.randint(3, 5)
    elif num_diff < 15:
        k = random.randint(4, 7)
    elif num_diff < 20:
        k = random.randint(5, 9)
    elif num_diff < 25:
        k = random.randint(6, 11)
    else:
        k = random.randint(7, 15)
    return k

def square_params_from_difficulty(num_diff):
    if num_diff < 5:
        return 10, False
    elif num_diff < 10:
        return 15, True
    elif num_diff < 15:
        return 20, True
    elif num_diff < 20:
        return 25, True
    elif num_diff < 25:
        return 30, True
    else:
        return 40, True
    
def near_boundary_param_from_difficulty(num_diff):
    if num_diff < 5:
        boundary = [10, 50]
        offset = 5
        ops = ["+"]
    elif num_diff < 10:
        boundary = [50, 100]
        offset = 10
        ops = ["+"]
    elif num_diff < 15:
        boundary = [100, 200]
        offset = 15
        ops = ["+", "-"]
    elif num_diff < 20:
        boundary = [200, 500]
        offset = 20
        ops = ["+", "-"]
    elif num_diff < 25:
        boundary = [500, 1000]
        offset = 30
        ops = ["+", "-"]
    else:
        boundary = [1000, 2000]
        offset = 50
        ops = ["+", "-"]
    return boundary, offset, ops
  
def near_square_offset(num_diff):
    if num_diff < 10:
        return [1]
    elif num_diff < 15:
        return [1, 2]
    elif num_diff < 20:
        return [1, 2, 3]
    elif num_diff < 25:
        return [1, 2, 3, 5]
    else:
        return [1, 2, 3, 5, 10]
    
def is_arithmetic(seq):
    if len(seq) < 3:
        return False
    d = seq[1] - seq[0]
    return all(seq[i+1] - seq[i] == d for i in range(len(seq)-1))

def is_multiplicative(seq):
    if len(seq) < 3 or 0 in seq:
        return False
    r = seq[1] / seq[0]
    return all(seq[i+1] / seq[i] == r for i in range(len(seq)-1))

def eval_boolean(expr, values):
    if isinstance(expr, str):
        return values[expr]
    if expr[0] == "NOT":
        return not eval_boolean(expr[1], values)
    op, left, right = expr
    if op == "AND":
        return eval_boolean(left, values) and eval_boolean(right, values)
    elif op == "OR":
        return eval_boolean(left, values) or eval_boolean(right, values)

def build_boolean_expression(vars_list, ops_count, allow_not):
    expr = random.choice(vars_list)
    for i in range(ops_count):
        op = random.choice(["AND", "OR"])
        right = random.choice(vars_list)
        if allow_not and random.choice([True, False]):
            right = ("NOT", right)
        expr = (op, expr, right)
    if allow_not and random.choice([True, False]):
        expr = ("NOT", expr)
    return expr

def render_boolean(expr):
    if isinstance(expr, str):
        return expr

    if expr[0] == "NOT":
        inner = expr[1]
        if isinstance(inner, str):
            return f"(NOT {inner})"
        else:
            return f"(NOT {render_boolean(inner)})"
    op, left, right = expr
    return f"({render_boolean(left)} {op} {render_boolean(right)})"

def propagate_truth(graph, true_sets):
    queue = deque(true_sets)
    inferred = set(true_sets)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in inferred:
                inferred.add(neighbor)
                queue.append(neighbor)
    return inferred

def is_relevant(base, graph):
    return base in graph or any(base in nbrs for nbrs in graph.values())

def build_graph(comparisons):
    graph = defaultdict(set)
    
    for a, op, b in comparisons:
        if op == ">":
            graph[a].add(b)
        elif op == "<":
            graph[b].add(a)
    return graph

def has_path(graph, start, end):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False
  
def is_trivial_query(x, y, constraints):
    return (x, y) in constraints or (y, x) in constraints

def generate_comparison(log_difficulty):
    no_of_objects = comparison_params_from_difficulty(log_difficulty)
    objects = list(string.ascii_uppercase[:no_of_objects])
    relation_word = random.choice(RELATIONS)
    line = ""
    comparisons = []
    
    true_order = objects[:]
    random.shuffle(true_order)
    
    for i in range(no_of_objects - 1):
        a = true_order[i]
        b = true_order[i + 1]
        if random.choice([True, False]):
            comparisons.append((a, ">", b))
        else:
            comparisons.append((b, "<", a))
    graph = build_graph(comparisons)
    while True:
        x, y = random.sample(objects, 2)
        if y in graph.get(x, set()) or x in graph.get(y, set()):
            continue
        if not has_path(graph, x, y) and not has_path(graph, y, x):
            continue
        break

    if has_path(graph, x, y):
        answer = "yes"
    elif has_path(graph, y, x):
        answer = "no"
    for a, op, b in comparisons:
        if op == ">":
            line += f"{a} is {relation_word} {b}. "
        elif op == "<":
            line += f"{b} is {relation_word} {a}. "
    line += f"Is {x} {relation_word} {y}?"
    question_text = line
    
    return {
        "task_id": f"LOG-COMP-{log_difficulty}-{no_of_objects}",
        "skill": "logical",
        "difficulty": log_difficulty,
        "question": question_text,
        "answer": answer
    }

def generate_boolean_evaluation(log_difficulty):
    vars_count, ops_count, allow_not = boolean_params_from_difficulty(log_difficulty)
    variables = list(string.ascii_uppercase[:vars_count])
    values = {v: random.choice([True, False]) for v in variables}
    expr = build_boolean_expression(variables, ops_count, allow_not)
    result = eval_boolean(expr, values)
    lines = []
    for v in variables:
        lines.append(f"{v} is {values[v]}.")
    lines.append(f"What is: {render_boolean(expr)}?")
    question_text = "\n".join(lines)
    return {
        "task_id": f"LOG-BOOL-{log_difficulty}-{vars_count}-{ops_count}",
        "skill": "logical",
        "difficulty": log_difficulty,
        "question": question_text,
        "answer": "True" if result else "False"
    }
 
def generate_implication_chain(log_difficulty):
    vars_count, edges = implication_params_from_difficulty(log_difficulty)
    variables = list(string.ascii_uppercase[:vars_count])
    while True: 
        graph = defaultdict(set)
        all_edges = set()
        while len(all_edges) < edges:
            a, b = random.sample(variables, 2)
            if a != b:
                all_edges.add((a, b))
        for a, b in all_edges:
            graph[a].add(b)
        base_true = set(random.sample(variables, random.randint(1, 2)))
        if not any(is_relevant(b, graph) for b in base_true):
            continue
        inferred = propagate_truth(graph, base_true)
        candidates = [
            v for v in variables
            if v not in base_true and is_relevant(v, graph)
        ]
        if not candidates:
            continue
        query = random.choice(candidates)
        answer = "yes" if query in inferred else "no"
        lines = []
        for v in base_true:
            lines.append(f"{v} is True.")
        for a, b in all_edges:
            lines.append(f"If {a} is True, then {b} is True.")
        lines.append(f"Is {query} True?")
        question_text = "\n".join(lines)
        break
    return {
        "task_id": f"LOG-IMP-{log_difficulty}-{vars_count}-{edges}",
        "skill": "logical",
        "difficulty": log_difficulty,
        "question": question_text,
        "answer": answer
    }
   
def generate_constraint_task(log_difficulty):
    n_objects, n_constraints = constraint_params_from_difficulty(log_difficulty)
    objects = list(string.ascii_uppercase[:n_objects])
    relation, inverse = random.choice(REL_WORDS)
    graph = defaultdict(set)
    constraints = set()
    
    while len(constraints) < n_constraints:
        a, b = random.sample(objects, 2)
        if has_path(graph, a, b):
            continue
        if (a, b) in constraints:
            continue
        if (b, a) in constraints:
            continue
        constraints.add((a, b))
        graph[a].add(b)
    query = None
    for _ in range(1000):
        x, y = random.sample(objects, 2)
        if x == y:
            continue
        if not (has_path(graph, x, y) or has_path(graph, y, x)):
            continue
        if is_trivial_query(x, y, constraints):
            continue
        query = (x, y)
        break
    if query is None:
        for _ in range(1000):
            x, y = random.sample(objects, 2)
            if has_path(graph, x, y) or has_path(graph, y, x):
                query = (x, y)
                break
    x, y = query
    answer = "yes" if has_path(graph, x, y) else "no"
    lines = []
    for a, b in constraints:
        lines.append(f"{a} is {relation} {b}.")
    lines.append(f"Is {x} {relation} {y}?")
    
    return {
        "task_id": f"LOG-CONSTRAINT-{log_difficulty}-{n_objects}-{n_constraints}",
        "skill": "logical",
        "difficulty": log_difficulty,
        "question": "\n".join(lines),
        "answer": answer
    }

def generate_multiplicative_progression(pat_difficulty):
    length, multipliers, start = mp_params_from_difficulty(pat_difficulty)
    multiplier = random.choice(multipliers)
    seq = [start * (multiplier ** i) for i in range(length)]
    answer = seq[-1] * multiplier
    if answer > 100000:
        return generate_multiplicative_progression(pat_difficulty)
    seq_text = ", ".join(str(x) for x in seq)

    return {
        "task_id": f"PAT-MP-{pat_difficulty}-{length}-{multiplier}",
        "skill": "pattern",
        "difficulty": pat_difficulty,
        "question": seq_text,
        "answer": answer
    }

def generate_arithmetic_progression(pat_difficulty):
    length, step_max = ap_params_from_difficulty(pat_difficulty)
    step = random.choice([i for i in range(-step_max, step_max + 1) if i != 0])
    start = random.randint(-50, 50)
    seq = [start + i * step for i in range(length)]
    answer = seq[-1] + step
    seq_text = ", ".join(str(x) for x in seq)

    return {
        "task_id": f"PAT-AP-{pat_difficulty}-{length}-{step_max}",
        "skill": "pattern",
        "difficulty": pat_difficulty,
        "question": seq_text,
        "answer": answer
    }
 
def generate_cycle_pattern(pat_difficulty):
    cycle_len, total_len = cycle_params_from_difficulty(pat_difficulty)
    while True:
        cycle = [random.randint(1, 20) for _ in range(cycle_len)]
        if is_arithmetic(cycle) or is_multiplicative(cycle):
            continue
        break
    seq = []
    for i in range(total_len):
        seq.append(cycle[i % cycle_len])
        
    answer = cycle[total_len % cycle_len]
    seq_text = ", ".join(str(x) for x in seq)
    return {
        "task_id": f"PAT-CP-{pat_difficulty}-{cycle_len}-{total_len}",
        "skill": "pattern",
        "difficulty": pat_difficulty,
        "question": seq_text,
        "answer": answer
    }

def generate_mixed_pattern(pat_difficulty):
    op_len, seq_len, k_max = mixed_params_from_difficulty(pat_difficulty)
    while True:
        ops = []
        for i in range(op_len):
            op_type = random.choice(["+", "*"])
            k = random.randint(2, k_max)
            ops.append((op_type, k))
        current = random.randint(1, 20)
        seq = [current]
        for i in range(1, seq_len):
            op, k = ops[(i - 1) % op_len]
            if op == "+":
                current += k
            elif op == "*":
                current *= k
            if current <= 0 or current > 100000:
                break
            seq.append(current)
        if len(seq) < seq_len:
            continue
        if is_arithmetic(seq) or is_multiplicative(seq):
            continue
        answer = current
        break
    seq.pop()
    seq_text = ", ".join(str(x) for x in seq)
    return {
        "task_id": f"PAT-MIXED-{pat_difficulty}-{op_len}-{seq_len}-{k_max}",
        "skill": "pattern",
        "difficulty": pat_difficulty,
        "question": seq_text,
        "answer": answer
    }
    
def generate_mental_division(num_diff):
    scale = random.choice([10, 20, 25, 50, 100])
    divisor = division_params_from_difficulty(num_diff) * scale
    answer = random.randint(2, 20)
    dividend = answer * divisor
    question = f"What is {dividend} divided by {divisor}?"
    return {
        "task_id": f"NUM-DIV-{num_diff}",
        "skill": "numerical",
        "difficulty": num_diff,
        "question": question,
        "answer": answer
    }
    
def generate_ratio_scaling(num_diff):
    k = ratio_params_from_difficulty(num_diff)
    a = random.randint(2, 10)
    b = a * k
    new_a = random.randint(2, 10)
    while new_a == a:
        new_a = random.randint(2, 10)
    answer = new_a * k
    question = f"{a} -> {b}, {new_a} -> ?"
    return {
        "task_id": f"NUM-RATIOSCALING-{num_diff}",
        "skill": "numerical",
        "difficulty": num_diff,
        "question": question,
        "answer": answer
    }

def generate_inverse_ratio_scaling(num_diff):
    k = ratio_params_from_difficulty(num_diff)
    a = random.randint(2, 10)
    b = a * k
    new_b = random.randint(2, 10) * k
    while new_b == b:
        new_b = random.randint(2, 10) * k
    answer = new_b // k
    question = f"{b} -> {a}, {new_b} -> ?"
    return {
        "task_id": f"NUM-RATIO-INVERSE-{num_diff}",
        "skill": "numerical",
        "difficulty": num_diff,
        "question": question,
        "answer": answer
    }
    
def generate_square_task(num_diff):
    n_max, allow_near = square_params_from_difficulty(num_diff)
    n = random.randint(2, n_max)
    if allow_near and random.choice([True, False]):
        offset = random.choice(near_square_offset(num_diff))
        sign = random.choice([-1, 1])
        base = n + sign * offset
        answer = base * base
        question = f"What is {base}^2?"
    else:
        answer = n * n
        question = f"What is {n}^2?"
    return {
        "task_id": f"NUM-SQUARE-{num_diff}",
        "skill": "numerical",
        "difficulty": num_diff,
        "question": question,
        "answer": answer
    }    

def generate_near_boundary_task(num_diff):
    boundary, offset, ops = near_boundary_param_from_difficulty(num_diff)
    boundary_value = random.choice(boundary)
    delta = random.randint(1, offset)
    sign = random.choice([-1, 1])
    a = boundary_value + sign * delta
    op = random.choice(ops)
    if num_diff >= 15:
        b_boundary = random.choice(boundary)
        b_delta = random.randint(1, offset)
        b = b_boundary + random.choice([-1, 1]) * b_delta
    else:
        b = random.randint(1, offset * 2)
    if op == "+":
        answer = a + b
        question = f"What is {a} + {b}?"
    else:
        if a < b:
            a, b = b, a
        answer = a - b
        question = f"What is {a} - {b}?"
    return {
        "task_id": f"NUM-NEARBOUNDARY-{num_diff}",
        "skill": "numerical",
        "difficulty": num_diff,
        "question": question,
        "answer": answer
    }
    

for d in [2, 7, 12, 18, 25, 30]:
    q = generate_comparison(d)
    print(f"Difficulty: {q['difficulty']}")
    print(f"Question: {q['question']}")
    print(f"Answer: {q['answer']}\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_arithmetic_progression(d)
    print("Difficulty:", d)
    print("Q:", q["question"])
    print("A:", q["answer"], "\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_multiplicative_progression(d)
    print("Difficulty:", d)
    print("Q:", q["question"])
    print("A:", q["answer"], "\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_cycle_pattern(d)
    print("Difficulty:", d)
    print("Q:", q["question"])
    print("A:", q["answer"], "\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_mixed_pattern(d)
    print("Difficulty:", d)
    print("Q:", q["question"])
    print("A:", q["answer"], "\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_boolean_evaluation(d)
    print("Difficulty:", d)
    print(q["question"])
    print("Answer:", q["answer"], "\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_implication_chain(d)
    print("Difficulty:", d)
    print(q["question"])
    print("Answer:", q["answer"], "\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_constraint_task(d)
    print("Difficulty:", d)
    print(q["question"])
    print("Answer:", q["answer"], "\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_mental_division(d)
    print(f"Difficulty: {q['difficulty']}")
    print(f"Question: {q['question']}")
    print(f"Answer: {q['answer']}\n")
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_ratio_scaling(d)
    print(f"Difficulty: {q['difficulty']}")
    print(f"Question: {q['question']}")
    print(f"Answer: {q['answer']}\n")    
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_inverse_ratio_scaling(d)
    print(f"Difficulty: {q['difficulty']}")
    print(f"Question: {q['question']}")
    print(f"Answer: {q['answer']}\n")  
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_square_task(d)
    print(f"Difficulty: {q['difficulty']}")
    print(f"Question: {q['question']}")
    print(f"Answer: {q['answer']}\n")    
for d in [2, 7, 12, 18, 25, 30]:
    q = generate_near_boundary_task(d)
    print(f"Difficulty: {q['difficulty']}")
    print(f"Question: {q['question']}")
    print(f"Answer: {q['answer']}\n")
    




