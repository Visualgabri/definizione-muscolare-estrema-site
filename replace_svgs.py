
file_path = r"c:/Users/visua/Google Drive/Job Personal Trainer/Sito 2026/atom-astro-main/src/components/BentoGrid.astro"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# We will replace blocks with single lines containing the image tag.
# We must process in reverse order of line numbers to avoid shifting indices.

# Block 3: Supporto Continuo (Lines 370-515 1-indexed -> 369-514 0-indexed)
# Verify start and end
if "<svg" in lines[369] and "</svg>" in lines[514]:
    print("Found Block 3")
    lines[369] = '<img src="/bento_community.png" alt="Supporto Continuo" class="w-full h-40 object-cover rounded-[--card-border-radius]" />\n'
    # Clear remaining lines
    for i in range(370, 515):
        lines[i] = ""
else:
    print(f"Block 3 mismatch: {lines[369].strip()} ... {lines[514].strip()}")

# Block 2: Nutrizione Personalizzata (Lines 223-285 1-indexed -> 222-284 0-indexed)
# Verify start and end
if "<div" in lines[222] and "</div>" in lines[284]:
    print("Found Block 2")
    lines[222] = '<img src="/bento_nutrition.png" alt="Nutrizione Personalizzata" class="aspect-video w-full object-cover rounded-[--card-border-radius]" />\n'
    # Clear remaining lines
    for i in range(223, 285):
        lines[i] = ""
else:
    print(f"Block 2 mismatch: {lines[222].strip()} ... {lines[284].strip()}")

# Block 1: Monitoraggio Costante (Lines 20-88 1-indexed -> 19-87 0-indexed)
# Verify start and end
if "<svg" in lines[19] and "</svg>" in lines[87]:
    print("Found Block 1")
    lines[19] = '<img src="/bento_tracking.png" alt="Monitoraggio Costante" class="aspect-video w-full object-cover rounded-[--card-border-radius]" />\n'
    # Clear remaining lines
    for i in range(20, 88):
        lines[i] = ""
else:
    print(f"Block 1 mismatch: {lines[19].strip()} ... {lines[87].strip()}")

# Filter out empty lines created by replacement (optional, but cleaner)
# Actually, keeping them as empty strings is fine, or we can filter.
# Let's filter them out to clean up the file.
new_lines = [line for line in lines if line != ""]

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
