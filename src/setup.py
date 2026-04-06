from setuptools import setup
import setup_translate

pkg = 'Extensions.WerbeZapper'
setup(name='enigma2-plugin-extensions-werbezapper',
       version='3.0',
       description='Werbezapper-Plugin for Enigma2',
       package_dir={pkg: 'WerbeZapper'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'LICENSE']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
