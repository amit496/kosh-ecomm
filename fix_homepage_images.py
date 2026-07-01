from pathlib import Path

path = Path(r'c:\xampp\htdocs\kosh-ecomm\wp-content\themes\woothemes\custom-templates\homepage.php')
text = path.read_text(encoding='utf-8')
text = text.replace('get_header(); ?> ?>', 'get_header();\n$woothemes_theme_uri = get_stylesheet_directory_uri();\n$woothemes_assets_uri = $woothemes_theme_uri . \'/assets\';\n?>')
replacements = {
    'src="./images/': 'src="<?php echo esc_url( $woothemes_theme_uri ); ?>/images/',
    'data-srcset="./images/': 'data-srcset="<?php echo esc_url( $woothemes_theme_uri ); ?>/images/',
    'srcset="./images/': 'srcset="<?php echo esc_url( $woothemes_theme_uri ); ?>/images/',
    'data-src="./images/': 'data-src="<?php echo esc_url( $woothemes_theme_uri ); ?>/images/',
    'src=./images/': 'src="<?php echo esc_url( $woothemes_theme_uri ); ?>/images/',
    'data-src=./images/': 'data-src="<?php echo esc_url( $woothemes_theme_uri ); ?>/images/',
    'src="./assets/images/': 'src="<?php echo esc_url( $woothemes_assets_uri ); ?>/images/',
    'data-srcset="./assets/images/': 'data-srcset="<?php echo esc_url( $woothemes_assets_uri ); ?>/images/',
    'srcset="./assets/images/': 'srcset="<?php echo esc_url( $woothemes_assets_uri ); ?>/images/',
    'data-src="./assets/images/': 'data-src="<?php echo esc_url( $woothemes_assets_uri ); ?>/images/',
    'src=./assets/images/': 'src="<?php echo esc_url( $woothemes_assets_uri ); ?>/images/',
}
for old, new in replacements.items():
    text = text.replace(old, new)
text = text.replace('/images//', '/images/')
path.write_text(text, encoding='utf-8')
print('homepage.php patched')
