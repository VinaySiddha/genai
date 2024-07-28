import ollama

response = ollama.generate(
    model='llama3.1',
    prompt='what is a qubit?'
)
print(response)


{
 'model': 'llama3.1',
 'created_at': '2024-07-28T02:54:21.044485Z', 
 'response': 'Qubits, also known as quantum bits, are the fundamental units of information in quantum computing. They\'re like the "bits" (1s and 0s) you use to store data on classical computers, but with some key differences.\n\n**The Basics:**\n\nA qubit is a quantum system that can exist in multiple states simultaneously. This is known as a **superposition** of states. In other words, a qubit can represent both 0 and 1 at the same time!\n\nFor example, if you have a coin that\'s heads or tails, it\'s either one or the other. But with a qubit, it\'s like having two coins simultaneously: heads AND tails.\n\n**Quantum States:**\n\nA qubit is typically represented as a linear combination of the following three states:\n\n1. **|0›** (the "zero" state)\n2. **|1›** (the "one" state)\n3. **|+› = 1/√2 (|0› + |1›)** (the "plus" state, where it\'s both 0 and 1 at the same time)\n\n**Key Features:**\n\nHere are some essential properties of qubits:\n\n*   **Superposition**: A qubit can exist in multiple states simultaneously.\n*   **Entanglement**: Qubits can become "entangled," meaning their properties are connected, even when they\'re far apart.\n*   **Quantum Interference**: Qubits can exhibit quantum interference patterns, which allow them to perform certain calculations more efficiently than classical computers.\n\n**Qubits in Practice:**\n\nResearchers have created qubits using various physical systems, such as:\n\n1.  **Superconducting circuits**: Tiny loops of superconducting material that can store a magnetic field.\n2.  **Ion traps**: Traps that confine individual atoms or ions to create a "quantum well."\n3.  **Quantum dots**: Small particles made from semiconductor materials, which can be used as qubits.\n\nWhile qubits are still in the early stages of development, they have tremendous potential for revolutionizing computing and information processing.', 
 'done': True, 
 'done_reason': 'stop', 
 'context': [128006, 882, 128007, 271, 12840, 374, 264, 2874, 60320, 30, 128009, 128006, 78191, 128007, 271, 27, 2201, 907, 29, 48, 82502, 11, 1101, 3967, 439, 31228, 9660, 11, 527, 279, 16188, 8316, 315, 2038, 304, 31228, 25213, 13, 2435, 2351, 1093, 279, 330, 11777, 1, 320, 16, 82, 323, 220, 15, 82, 8, 499, 1005, 311, 3637, 828, 389, 29924, 19002, 11, 719, 449, 1063, 1401, 12062, 382, 334, 791, 68276, 25, 57277, 32, 2874, 60320, 374, 264, 31228, 1887, 430, 649, 3073, 304, 5361, 5415, 25291, 13, 1115, 374, 3967, 439, 264, 3146, 9712, 3571, 334, 315, 5415, 13, 763, 1023, 4339, 11, 264, 2874, 60320, 649, 4097, 2225, 220, 15, 323, 220, 16, 520, 279, 1890, 892, 2268, 2520, 3187, 11, 422, 499, 617, 264, 16652, 430, 596, 14971, 477, 64614, 11, 433, 596, 3060, 832, 477, 279, 1023, 13, 2030, 449, 264, 2874, 60320, 11, 433, 596, 1093, 3515, 1403, 19289, 25291, 25, 14971, 3651, 64614, 382, 334, 45320, 372, 4273, 25, 57277, 32, 2874, 60320, 374, 11383, 15609, 439, 264, 13790, 10824, 315, 279, 2768, 2380, 5415, 1473, 16, 13, 3146, 91, 15, 69209, 334, 320, 1820, 330, 14486, 1, 1614, 340, 17, 13, 3146, 91, 16, 69209, 334, 320, 1820, 330, 606, 1, 1614, 340, 18, 13, 3146, 91, 10, 69209, 284, 220, 16, 14, 110682, 17, 320, 91, 15, 69209, 489, 765, 16, 69209, 33395, 320, 1820, 330, 7284, 1, 1614, 11, 1405, 433, 596, 2225, 220, 15, 323, 220, 16, 520, 279, 1890, 892, 696, 334, 1622, 20289, 25, 57277, 8586, 527, 1063, 7718, 6012, 315, 2874, 82502, 1473, 9, 256, 3146, 19841, 3571, 96618, 362, 2874, 60320, 649, 3073, 304, 5361, 5415, 25291, 627, 9, 256, 3146, 2300, 526, 1001, 96618, 1229, 82502, 649, 3719, 330, 306, 40040, 1359, 7438, 872, 6012, 527, 8599, 11, 1524, 994, 814, 2351, 3117, 10980, 627, 9, 256, 3146, 45320, 372, 5783, 2251, 96618, 1229, 82502, 649, 31324, 31228, 32317, 12912, 11, 902, 2187, 1124, 311, 2804, 3738, 29217, 810, 30820, 1109, 29924, 19002, 382, 334, 48, 82502, 304, 28082, 25, 57277, 60210, 617, 3549, 2874, 82502, 1701, 5370, 7106, 6067, 11, 1778, 439, 1473, 16, 13, 220, 3146, 19841, 77752, 287, 46121, 96618, 49074, 30853, 315, 2307, 77752, 287, 3769, 430, 649, 3637, 264, 24924, 2115, 627, 17, 13, 220, 3146, 46580, 45660, 96618, 1183, 2690, 430, 2389, 483, 3927, 33299, 477, 65125, 311, 1893, 264, 330, 31548, 372, 1664, 10246, 18, 13, 220, 3146, 45320, 372, 32094, 96618, 15344, 19252, 1903, 505, 87836, 7384, 11, 902, 649, 387, 1511, 439, 2874, 82502, 382, 8142, 2874, 82502, 527, 2103, 304, 279, 4216, 18094, 315, 4500, 11, 814, 617, 28040, 4754, 369, 14110, 4954, 25213, 323, 2038, 8863, 13],
 'total_duration': 107709343900, 
 'load_duration': 47279500, 
 'prompt_eval_count': 20, 
 'prompt_eval_duration': 1230908000, 
 'eval_count': 435, 
 'eval_duration': 106428175000
}