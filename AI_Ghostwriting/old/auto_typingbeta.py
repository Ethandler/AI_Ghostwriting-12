import pyautogui
import time
import random
import string

# Enable the fail-safe: move your mouse to a screen corner to abort.
pyautogui.FAILSAFE = True

def get_wrong_character(correct_char):
    """
    Return a random character different from the intended one.
    For letters and digits, choose from a similar pool. For punctuation, choose randomly.
    """
    if correct_char.isalpha():
        letters = list(string.ascii_lowercase)
        # Remove the intended character (ignore case)
        try:
            letters.remove(correct_char.lower())
        except ValueError:
            pass
        return random.choice(letters)
    elif correct_char.isdigit():
        digits = list(string.digits)
        try:
            digits.remove(correct_char)
        except ValueError:
            pass
        return random.choice(digits)
    else:
        return random.choice(string.punctuation)

print("Focus the window where you want the text to be typed. You have 5 seconds...")
time.sleep(5)

text_to_type = (
     "for control of dwindling reserves, leading to widespread famine, disease, and resource wars. The Catalyst: A massive ecological collapse triggers a cascading effect, leaving the planet uninhabitable. 2. The Technological Catastrophe: The Trigger:" 
  "An unforeseen failure in AI-driven technologies like self-driving cars or power grids.The Conflict: Uncontrolled AI systems trigger a domino effect of malfunctions, causing blackouts, transportation chaos, and economic collapse.The Catalyst: The panic and societal breakdown lead to mass hysteria and social unrest, culminating in a nuclear winter. 3. The Bioengineered Apocalypse:"
  "The Trigger: The release of genetically modified organisms (GMOs) that escape into the environment and wreak havoc. The Conflict: The GMOs become invasive species, outcompeting native plants and animals, disrupting ecosystems and triggering pandemics. The Catalyst: Mass extinction events occur as the GMOs decimate biodiversity and disrupt food chains.4. The Cosmic Calamity:"
  "The Trigger: A large asteroid impact with Earth, triggered by an unstable solar system.The Conflict: The impact creates a devastating dust cloud, blocking sunlight and plunging the planet into darkness.The Catalyst: Global temperatures plummet, triggering a prolonged ice age and wiping out most life forms. 5. The Pandemic Plague:"
  "The Trigger: A highly contagious and deadly pandemic caused by a mutated virus.The Conflict: The virus spreads rapidly, overwhelming healthcare systems and creating widespread fear and panic.The Catalyst: The pandemic leads to social isolation, economic collapse, and mass casualties, leaving humanity vulnerable. 6. The Nuclear Nightmare:"
  "The Trigger: Escalation of geopolitical tensions, leading to multiple nuclear warheads being deployed.The Conflict: A chain reaction of retaliatory strikes results in a full-scale nuclear winter, blanketing the globe in ash and radiation.The Catalyst: Radiation sickness and long-term environmental damage cripple the human population. 7. The Climate Change Crisis:"
  "The Trigger: Continued inaction on climate change leads to catastrophic consequences like rising sea levels, extreme weather events, and mass migrations. The Conflict: Resources become scarce, leading to conflicts between nations and within communities. The Catalyst: Extreme heat waves, droughts, and floods cause widespread famine and mass displacement, leading to social breakdown. 8. The Social Collapse:"
  "The Trigger: Decades of political instability, economic inequality, and cultural divisions create widespread distrust and violence. The Conflict: People lose faith in institutions and governments, leading to civil unrest and social disintegration. The Catalyst:  Breakdown of law and order, followed by a loss of trust in each other, ultimately leading to the collapse of society. 9. The Alien Invasion:"
  "The Trigger: Extraterrestrial life arrives on Earth, either peacefully or aggressively seeking resources or dominance. The Conflict: Humans face off against advanced alien technology, leading to warfare, exploitation, or assimilation. The Catalyst:  Alien interference disrupts our technological advancement and throws our civilization into chaos. 10. The Self-Inflicted Wound:"
  "The Trigger: Humanity continues down a path of unsustainable consumption and neglect, ignoring warnings about its future. The Conflict: Resources dwindle, pollution intensifies, and natural disasters become more frequent.  The Catalyst:  Humanity's own actions lead to its own demise through environmental degradation, resource depletion, and societal collapse."


)
# Loop through each character in the text.
for char in text_to_type:
    # Decide if a typo should occur (5% chance), and only for visible characters.
    if char.strip() and random.random() < 0.05:
        # Simulate typing the wrong character.
        wrong_char = get_wrong_character(char)
        pyautogui.write(wrong_char)
        # Wait a short moment before correcting.
        time.sleep(random.uniform(0.010, 0.025))
        # Simulate backspace to erase the wrong character.
        pyautogui.press('backspace')
        # Short pause before retyping the correct character.
        time.sleep(random.uniform(0.1, 0.2))
        pyautogui.write(char)
    else:
        pyautogui.write(char)
    
    # Delay to simulate human typing speed (averaging about 0.387 seconds per character).
    time.sleep(random.uniform(0.019, 0.18))

print("Finished typing.")