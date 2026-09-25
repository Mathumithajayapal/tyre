import os

files = ["index.html", "home-2.html", "about.html"]

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # CSS tweaks
        content = content.replace('padding: 0 32px; height: 90px;', 'padding: 0 16px; height: 90px;')
        
        # Typography scaling fixes
        content = content.replace('text-5xl md:text-7xl lg:text-8xl', 'text-4xl md:text-6xl xl:text-7xl')
        content = content.replace('text-4xl lg:text-5xl', 'text-4xl xl:text-5xl')
        content = content.replace('lg:text-4xl', 'xl:text-4xl')
        
        # Grid tweaks to allow wrapping on mobile
        content = content.replace('grid-cols-2 gap-8', 'grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-8')
        content = content.replace('grid-cols-2 gap-6', 'grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6')
        
        # Breakpoint adjustments to prevent cramping at 1024px
        content = content.replace('lg:flex-row', 'xl:flex-row')
        content = content.replace('lg:flex-row-reverse', 'xl:flex-row-reverse')
        content = content.replace('lg:w-1/2', 'xl:w-1/2')
        content = content.replace('lg:w-1/3', 'xl:w-1/3')
        content = content.replace('lg:w-2/3', 'xl:w-2/3')
        content = content.replace('lg:px-12', 'xl:px-12')
        content = content.replace('lg:p-24', 'xl:p-24')
        content = content.replace('lg:grid-cols-3', 'xl:grid-cols-3')
        content = content.replace('lg:grid-cols-4', 'xl:grid-cols-4')
        content = content.replace('lg:divide-y-0', 'xl:divide-y-0')
        content = content.replace('lg:divide-x', 'xl:divide-x')
        content = content.replace('lg:col-span-4', 'xl:col-span-4')
        content = content.replace('lg:col-span-8', 'xl:col-span-8')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
    except Exception as e:
        print(f"Error on {file}: {e}")
