GROUPS := glib gluch gulag gultec gultij linuxcabal lugags mxlos ranchoelectronico

GROUPS_YAML := $(patsubst %,src/%.yaml,$(GROUPS))
GROUPS_RST := $(patsubst src/%.yaml,src/build/%.rst,$(GROUPS_YAML))

all: $(GROUPS_RST) src/build/main.rst test pdf/directorio.pdf

src/build/%.rst: src/%.yaml
	@mkdir -p src/build
	src/build.py < $< > $@

src/build/main.rst: GNUmakefile
	@mkdir -p src/build
	echo ".. include:: ../header.rst" > src/build/main.rst
	echo "" >> src/build/main.rst
	for G in $(GROUPS); do echo ".. include:: $$G.rst" >> src/build/main.rst; done
	echo "" >> src/build/main.rst
	echo ".. include:: ../footer.rst" >> src/build/main.rst

pdf/directorio.pdf: src/build/main.rst
pdf/directorio.pdf: src/header.rst
pdf/directorio.pdf: src/footer.rst
pdf/directorio.pdf: $(GROUPS_RST)
pdf/directorio.pdf:
	mkdir -p pdf
	rst2pdf src/build/main.rst -o pdf/directorio.pdf

clean:
	rm -f pdf/directorio.pdf
	-[ ! -d pdf ] || rmdir pdf
	rm -f passed/*
	-[ ! -d passed ] || rmdir passed
	rm -f $(GROUPS_RST) src/build/main.rst
	-[ ! -d src/build ] || rmdir src/build

test:
