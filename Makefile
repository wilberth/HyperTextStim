build/lib/hypertextstim/hypertextstim.py: hypertextstim.py	
	python3 setup.py bdist_wheel

clean:
	rm -rf build dist HyperTextStim.egg-info

