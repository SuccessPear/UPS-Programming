import matplotlib.pyplot as plt

def draw_top_level_entity():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Draw blocks for Input Signals
    ax.text(1, 8, 'LoadA', ha='center', va='center', bbox=dict(facecolor='skyblue', edgecolor='black'))
    ax.text(1, 7, 'Reset', ha='center', va='center', bbox=dict(facecolor='skyblue', edgecolor='black'))
    ax.text(1, 6, 'Clock', ha='center', va='center', bbox=dict(facecolor='skyblue', edgecolor='black'))

    # Draw blocks for Top-Level FSM
    ax.text(5, 7, 'FSM Circuit', ha='center', va='center', bbox=dict(facecolor='lightgreen', edgecolor='black'))

    # Draw blocks for Output Signals
    ax.text(9, 8, 'Done', ha='center', va='center', bbox=dict(facecolor='lightcoral', edgecolor='black'))
    ax.text(9, 7, 'Result', ha='center', va='center', bbox=dict(facecolor='lightcoral', edgecolor='black'))

    # Draw arrows
    ax.arrow(1.5, 8, 2.5, 0, head_width=0.2, head_length=0.4, fc='black', ec='black')
    ax.arrow(1.5, 7, 2.5, 0, head_width=0.2, head_length=0.4, fc='black', ec='black')
    ax.arrow(1.5, 6, 2.5, 0, head_width=0.2, head_length=0.4, fc='black', ec='black')
    ax.arrow(7, 7, 2.5, 1, head_width=0.2, head_length=0.4, fc='black', ec='black')
    ax.arrow(7, 7, 2.5, 0, head_width=0.2, head_length=0.4, fc='black', ec='black')

    plt.show()

draw_top_level_entity()
