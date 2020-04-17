# controlaPy
Platform to control and follow all procurement of a goverment
#### URL

https://controlapy.org

## Requirements

* Python 3.6+
* Django 2.2+
* PostreSQL 12.0+

## Install

```
git clone git@github.com:controlapy/controlapy.git
cd controlapy
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp conf/.env.example conf/.env # you should edit this file with your configuration
./manage.py migrate
./manage.py runserver
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Author

* Contraloría Ciudadana https://github.com/controlapy

## Contributors / Thanks

* Carlos Aguilar https://github.com/gomezag

## TODO

More in [TODO.md](TODO.md)

## License

This project is licensed under the terms of the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details