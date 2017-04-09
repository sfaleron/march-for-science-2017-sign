
OBJS = copyleft.pdf assembly.pdf

all: $(OBJS)

%.pdf : %.svg
	inkscape -C -y 255 --export-pdf=$@ $<
