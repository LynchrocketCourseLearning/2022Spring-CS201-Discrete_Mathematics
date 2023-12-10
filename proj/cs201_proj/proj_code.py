from manim import *

PYTHON_CODE = \
'''
def dijkstra(s):
    distance[s] = 0
    q = PriorityQueue(V)
    q.put_nowait(s)
    while q.qsize()!=0:
        v = q.get_nowait()
        visited[v] = True
        for u in range(V):
            if graph[v][u] == math.inf or visited[u]:
                continue
            else:
                q.put_nowait(u)
            if distance[u] > distance[v] + graph[v][u]:
                distance[u] = distance[v] + graph[v][u]
'''

class Dijkstra(Scene):
    def construct(self):
        self.video_start()
        self.menu()
        self.intro()
        self.dijkstra()
        self.source_code()
        self.reference()
        self.video_end()

    def video_start(self):
        title = Text(
            'Dijkstra\'s Algorithm',
            gradient = [BLUE, GREEN]
        ).scale(1.5)
        title.to_corner((ORIGIN + 4 * UP))

        subtitle = Text('CS201 Discrete Mathematics: Final project')
        subtitle.next_to(title, DOWN, buff=0.75)

        author = Text(
            'Liu Leqi'
        ).scale(0.75)
        author.next_to(subtitle, DOWN, buff=1.5)

        self.play(
            Write(title)
        )
        self.play(
            Write(subtitle),
            Write(author)
        )
        self.wait()

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(author),
            run_time=0.5
        )

    def menu(self):
        topics = VGroup(
            Text('Introduction to the problem'),
            Text('Dijkstra\'s Algorithm'),
            Text('Source code'),
            Text('Reference')
        )
        for topic in topics:
            dot = Dot(color=BLUE)
            dot.next_to(topic, LEFT)
            topic.add(dot)
        
        topics.arrange(
            DOWN, aligned_edge=LEFT, buff=LARGE_BUFF
        ).move_to(LEFT)
        self.add(topics)
        self.wait(2)

        length_of_topics = len(topics)
        for i in range(length_of_topics):
            self.play(
                FadeOut(topics[length_of_topics-i-1])
            )

        # for i in range(len(topics)):
        #     self.play(
        #         topics[i + 1:].set_fill, {"opacity": 0.25},
        #         topics[:i].set_fill, {"opacity": 0.25},
        #         topics[i].set_fill, {"opacity": 1}
        #     )
        #     self.wait(2)

    vertices = ['a','b','c','d','e']
    edges = [('b','c'),('a','b'),('d','e'),('d','b'),('d','c'),('c','e'),('a','d'),('e','a')]

    def intro(self):
        title = Title("Introduction to the problem").set_color(BLUE)
        self.play(Create(title))
        self.wait(2)
        problem = Text(
            'Given a directed graph with weight, \n find a shortest path from source vertex to any other vertex',
            line_spacing=0.6
        ).scale(0.5).move_to((ORIGIN+UL*2))
        self.play(Write(problem))
        self.wait()

        graph = Graph(
            self.vertices, self.edges,
            labels=True, edge_type=Arrow,
            edge_config={
                'stroke_width':3.5,
                ('b','c'):{'color':WHITE},
                ('a','b'):{'color':BLUE},
                ('d','e'):{'color':BLUE},
                ('d','b'):{'color':YELLOW},
                ('d','c'):{'color':YELLOW},
                ('c','e'):{'color':GREEN},
                ('a','d'):{'color':RED},
                ('e','a'):{'color':RED}
            }
        ).move_to((ORIGIN+DOWN*1.5))
        self.play(Create(graph))
        question = Text(
            'How can we do that?'
        ).scale(0.5).move_to((ORIGIN+DL*3))
        self.play(
            FadeOut(title),
            problem.animate.to_corner(UL),
            graph.animate.change_layout('circular'),
            Write(question)
        )
        self.wait()

        self.play(
            FadeOut(question),
            FadeOut(graph),
            FadeOut(problem)
        )

    def dijkstra(self):
        title = Title("Dijkstra\'s Algorithm").set_color(BLUE)
        self.play(Create(title))
        self.wait(2)

        # describe the algorithm roughly
        describe = Text(
            'As the graph shown on the right, we use (color, weight): \n(WHITE, 1), (BLUE, 2), (YELLOW, 3), (GREEN, 4), (RED, 5)',
            line_spacing=0.6
        ).scale(0.5).move_to((ORIGIN+UL*2))
        self.play(Write(describe))
        self.wait()

        graph = Graph(
            self.vertices, self.edges,
            labels=True, edge_type=Arrow,
            layout='circular',
            edge_config={
                'stroke_width':3,
                ('b','c'):{'color':WHITE},
                ('a','b'):{'color':BLUE},
                ('d','e'):{'color':BLUE},
                ('d','b'):{'color':YELLOW},
                ('d','c'):{'color':YELLOW},
                ('c','e'):{'color':GREEN},
                ('a','d'):{'color':RED},
                ('e','a'):{'color':RED}
            }
        ).move_to((ORIGIN+RIGHT*4+DOWN))

        d1 = Text(
            'Dijkstra\'s algorithm is a kind of greedy algorithm.'
        ).scale(0.5).move_to((ORIGIN+UL*2))
        d2 = Text(
            'It starts from source vertex and vertex set S.'
        ).scale(0.5).move_to((ORIGIN+UL*2))
        d3 = Text(
            'Every iteration it extracts a vertex that has \na shortest path to the source.',
            line_spacing=0.5
        ).scale(0.5).move_to((ORIGIN+UL*2))
        d4 = Text(
            'However, it needs the weights to be positive.'
        ).scale(0.5).move_to((ORIGIN+UL*2))

        algorithm_describe = VGroup(d1,d2,d3,d4).arrange(
            DOWN, aligned_edge=LEFT, buff=SMALL_BUFF
        ).move_to(LEFT*3)

        self.play(
            Create(graph),
            Write(algorithm_describe),
            run_time=2.5
        )
        self.wait(2)

        # start the algorithm
        weight_describe = Text(
            'Source is vertex a. \n(WHITE, 1), (BLUE, 2), (YELLOW, 3), (GREEN, 4), (RED, 5)',
            line_spacing=0.6
        ).scale(0.5).to_corner(UL)
        t = [
                ['a','0','null'],
                ['b','infty','null'],
                ['c','infty','null'],
                ['d','infty','null'],
                ['e','infty','null']
            ]
        table1 = Table(
            table=t,
            col_labels=[Text('vertex v'), Text('distance(v)'), Text('parent(v)')]
        ).scale(0.5).move_to((ORIGIN+RIGHT*4))

        self.play(
            FadeOut(title),
            FadeOut(algorithm_describe),
            Transform(describe, weight_describe),
            graph.animate.move_to((ORIGIN+LEFT*4)),
            table1.create()
        )
        self.wait(2)

        # iteration 1
        s11 = Text('Start from source vertex a').scale(0.5).move_to((ORIGIN+DOWN*3))
        s12 = Text('Relax the out-going edges of a').scale(0.5).move_to((ORIGIN+DOWN*3))
        t[1][1], t[3][1] = '2', '5'
        t[1][2], t[3][2] = 'a', 'a'
        table2 = Table(
            table=t,
            col_labels=[Text('vertex v'), Text('distance(v)'), Text('parent(v)')]
        ).scale(0.5).move_to((ORIGIN+RIGHT*4))
        table2.add_highlighted_cell((2,1),color=GREEN)

        self.play(
            Write(s11),
            table1.animate.add_highlighted_cell((2,1),color=GREEN)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(s11,s12),
            ReplacementTransform(table1, table2)
        )
        self.wait(2)

        # iteration 2
        s21 = Text('Turn to vertex b').scale(0.5).move_to((ORIGIN+DOWN*3))
        s22 = Text('Relax the out-going edges of b').scale(0.5).move_to((ORIGIN+DOWN*3))
        t[2][1], t[2][2] = '3', 'b'
        table1 = Table(
            table=t,
            col_labels=[Text('vertex v'), Text('distance(v)'), Text('parent(v)')]
        ).scale(0.5).move_to((ORIGIN+RIGHT*4))
        table1.add_highlighted_cell((2,1),color=GREEN)
        table1.add_highlighted_cell((3,1),color=GREEN)
        
        self.play(
            ReplacementTransform(s12,s21),
            table2.animate.add_highlighted_cell((3,1),color=GREEN)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(s21,s22),
            ReplacementTransform(table2, table1)
        )
        self.wait(2)

        # iteration 3
        s31 = Text('Turn to vertex c').scale(0.5).move_to((ORIGIN+DOWN*3))
        s32 = Text('Relax the out-going edges of c').scale(0.5).move_to((ORIGIN+DOWN*3))
        t[4][1], t[4][2] = '7', 'c'
        table2 = Table(
            table=t,
            col_labels=[Text('vertex v'), Text('distance(v)'), Text('parent(v)')]
        ).scale(0.5).move_to((ORIGIN+RIGHT*4))
        table2.add_highlighted_cell((2,1),color=GREEN)
        table2.add_highlighted_cell((3,1),color=GREEN)
        table2.add_highlighted_cell((4,1),color=GREEN)
        
        self.play(
            ReplacementTransform(s22,s31),
            table1.animate.add_highlighted_cell((4,1),color=GREEN)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(s31,s32),
            ReplacementTransform(table1, table2)
        )
        self.wait(2)

        # iteration 4
        s41 = Text('Turn to vertex d').scale(0.5).move_to((ORIGIN+DOWN*3))
        s42 = Text('Relax the out-going edges of d. Here no need to relax.').scale(0.5).move_to((ORIGIN+DOWN*3))
        
        self.play(
            ReplacementTransform(s32,s41),
            table2.animate.add_highlighted_cell((5,1),color=GREEN)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(s41,s42)
        )
        self.wait(2)

         # iteration 5
        s51 = Text('Turn to vertex e').scale(0.5).move_to((ORIGIN+DOWN*3))
        s52 = Text('Relax the out-going edges of e. Here no need to relax.').scale(0.5).move_to((ORIGIN+DOWN*3))
        
        self.play(
            ReplacementTransform(s42,s51)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(s51,s52)
        )
        self.wait(3)

        self.clear()

    def source_code(self):
        title = Title("Source code").set_color(BLUE)
        self.play(Create(title))
        self.wait(2)
        code_kwargs = {
            "code"        :    PYTHON_CODE,
            "tab_width"   :    4,
            "background"  :    "window",
            "language"    :    "Python",
            "font"        :    "Monospace",
            "font_size"   :    20,
            "style"       :    "monokai"
        }
        code = Code(**code_kwargs)
        code.move_to(ORIGIN)
        self.draw_code_all_lines_at_a_time(code,run_time=3)
        self.wait()
        self.play(
            FadeOut(title, shift=UP),
            code.animate.to_edge(UP, buff=0).scale(0.8)
        )
        self.wait()

        frame = Rectangle(
            width=config["frame_width"]*0.8,
            height=config["frame_height"]*0.4,
        )
        frame.next_to(code,DOWN)
        FRAME_SCALE = 0.45
        FRAME_CENTER = frame.get_center()

        # ShowCreation -> Create
        line = self.get_remark_rectangle(code, 1)

        # def dijkstra(s):
        line.save_state()
        line.stretch(0.01,0) # set_width(0.01,0) 0 is x direction
        # line.set_fill(opacity=0)
        self.add(line)
        self.play(Restore(line))
        self.wait()
        self.play(Create(frame))
        graph = Graph(
            self.vertices, self.edges,
            labels=True, edge_type=Arrow,
            layout='circular',
            edge_config={
                'stroke_width':3,
                ('b','c'):{'color':WHITE},
                ('a','b'):{'color':BLUE},
                ('d','e'):{'color':BLUE},
                ('d','b'):{'color':YELLOW},
                ('d','c'):{'color':YELLOW},
                ('c','e'):{'color':GREEN},
                ('a','d'):{'color':RED},
                ('e','a'):{'color':RED}
            }
        ).scale(FRAME_SCALE).move_to((FRAME_CENTER+LEFT*3.5))
        self.play(Create(graph))
        self.wait(0.5)
        matrix = Matrix(
            [
                [0,2,0,5,0],
                [0,0,1,0,0],
                [0,0,0,0,4],
                [0,3,3,0,2],                
                [5,0,0,0,0]
            ]
        ).scale(FRAME_SCALE).move_to((FRAME_CENTER+LEFT*3.5))
        entries = matrix.get_entries()
        self.play(
            FadeOut(graph),
            FadeIn(matrix)
        )

        # distance[s] = 0
        self.change_line(code, line, 2)
        t = [
                ['a','b','c','d','e'],
                ['0','inf','inf','inf','inf']
            ]
        table1 = Table(
            table=t,
            row_labels=[Text('vertex v'), Text('distance(v)')]
        ).scale(0.35).move_to((FRAME_CENTER+RIGHT*2.5+UP))
        self.play(table1.create())

        # q = PriorityQueue(V)
        self.change_line(code, line, 3)

        # q.put_nowait(s)
        self.change_line(code, line, 4)
        rectangle1 = Rectangle().scale(FRAME_SCALE*0.75).move_to(frame, aligned_edge=DOWN)
        bg_rec1 = BackgroundRectangle(rectangle1, color=YELLOW, stroke_width=1)
        rec_label1 = Text('a').scale(0.5).next_to(bg_rec1, ORIGIN)
        queue_element1 = VGroup(bg_rec1, rec_label1)
        self.play(FadeIn(queue_element1, shift=DOWN))
        
        # while q.qsize()!=0:
        self.change_line(code, line, 5)

        # v = q.get_nowait()
        self.change_line(code, line, 6)
        circle = Circle().scale(0.2).next_to(queue_element1, RIGHT)
        circ_label = Text('a').scale(0.5).next_to(circle, ORIGIN)
        vertex_element = VGroup(circle, circ_label)
        self.play(ReplacementTransform(queue_element1, vertex_element))

        # visited[v] = True
        self.change_line(code, line, 7)

        # for u in range(V):
        self.change_line(code, line, 8)
        # if graph[v][u] == math.inf or visited[u]:
        #     continue
        # else:
        #     q.put_nowait(u)
        self.change_line(code, line, 9) # if graph[v][u] == math.inf or visited[u]:
        self.play(matrix.animate.add(SurroundingRectangle(entries[0])))
        
        self.change_line(code, line, 10) # continue

        self.change_line(code, line, 8) # for u in range(V):
        self.change_line(code, line, 9) # if graph[v][u] == math.inf or visited[u]:
        self.play(matrix.animate.add(SurroundingRectangle(entries[1])))
        self.change_line(code, line, 11) # else:
        self.change_line(code, line, 12) # q.put_nowait(u)
        rectangle1 = Rectangle().scale(FRAME_SCALE*0.75).move_to(frame, aligned_edge=DOWN)
        bg_rec1 = BackgroundRectangle(rectangle1, color=YELLOW, stroke_width=1)
        rec_label1 = Text('b').scale(0.5).next_to(bg_rec1, ORIGIN)
        queue_element1 = VGroup(bg_rec1, rec_label1)
        self.play(FadeIn(queue_element1, shift=DOWN))
        
        # if distance[u] > distance[v] + graph[v][u]:
        #     distance[u] = distance[v] + graph[v][u]
        self.change_line(code, line, 13)
        self.change_line(code, line, 14)
        t[1][1] = '2'
        table2 = Table(
            table=t,
            row_labels=[Text('vertex v'), Text('distance(v)')]
        ).scale(0.35).move_to((FRAME_CENTER+RIGHT*2.5+UP))
        self.play(ReplacementTransform(table1, table2))

        # for u in range(V):
        self.change_line(code, line, 8)
        # if graph[v][u] == math.inf or visited[u]:
        #     continue
        # else:
        #     q.put_nowait(u)
        self.change_line(code, line, 9) # if graph[v][u] == math.inf or visited[u]:
        self.play(matrix.animate.add(SurroundingRectangle(entries[2])))
        self.change_line(code, line, 10) # continue

        self.change_line(code, line, 8) # for u in range(V):

        self.change_line(code, line, 9) # if graph[v][u] == math.inf or visited[u]:
        self.play(matrix.animate.add(SurroundingRectangle(entries[3])))
        self.change_line(code, line, 11) # else:
        self.change_line(code, line, 12) # q.put_nowait(u)
        rectangle2 = Rectangle().scale(FRAME_SCALE*0.75).next_to(rectangle1, UP, buff=0)
        bg_rec2 = BackgroundRectangle(rectangle2, color=ORANGE, stroke_width=1)
        rec_label2 = Text('d').scale(0.5).next_to(bg_rec2, ORIGIN)
        queue_element2 = VGroup(bg_rec2, rec_label2)
        self.play(FadeIn(queue_element2, shift=DOWN))
        
        # if distance[u] > distance[v] + graph[v][u]:
        #     distance[u] = distance[v] + graph[v][u]
        self.change_line(code, line, 13)
        self.change_line(code, line, 14)
        t[1][3] = '5'
        table1 = Table(
            table=t,
            row_labels=[Text('vertex v'), Text('distance(v)')]
        ).scale(0.35).move_to((FRAME_CENTER+RIGHT*2.5+UP))
        self.play(ReplacementTransform(table2, table1))

        # for u in range(V):
        self.change_line(code, line, 8)
        self.play(matrix.animate.add(SurroundingRectangle(entries[4])))
        self.play(FadeOut(vertex_element))

        # while q.qsize()!=0:
        self.change_line(code, line, 5)
        notice = Text(
            'For short, \nwe omit the \nremaining steps.',
            line_spacing=0.6
        ).scale(0.5).to_corner(UL)
        self.play(Write(notice))
        for i in range(len(entries)):
            if i <= 4:
                continue
            if i == 5:
                self.play(FadeOut(vertex_element))
                circle = Circle().scale(0.2).next_to(rectangle1, RIGHT)
                circ_label = Text('b').scale(0.5).next_to(circle, ORIGIN)
                vertex_element = VGroup(circle, circ_label)
                self.play(
                    ReplacementTransform(queue_element1, vertex_element),
                    queue_element2.animate.move_to(frame, aligned_edge=DOWN)
                )
            if i == 10:
                self.play(FadeOut(vertex_element))
                circle = Circle().scale(0.2).next_to(rectangle1, RIGHT)
                circ_label = Text('c').scale(0.5).next_to(circle, ORIGIN)
                vertex_element = VGroup(circle, circ_label)
                self.play(
                    ReplacementTransform(queue_element1, vertex_element)
                )
            if i == 15:
                self.play(FadeOut(vertex_element))
                circle = Circle().scale(0.2).next_to(rectangle1, RIGHT)
                circ_label = Text('d').scale(0.5).next_to(circle, ORIGIN)
                vertex_element = VGroup(circle, circ_label)
                self.play(
                    ReplacementTransform(queue_element2, vertex_element),
                    queue_element1.animate.move_to(frame, aligned_edge=DOWN)
                )
            if i == 20:
                self.play(FadeOut(vertex_element))
                circle = Circle().scale(0.2).next_to(rectangle1, RIGHT)
                circ_label = Text('e').scale(0.5).next_to(circle, ORIGIN)
                vertex_element = VGroup(circle, circ_label)
                self.play(
                    ReplacementTransform(queue_element1, vertex_element)
                )

            self.play(matrix.animate.add(SurroundingRectangle(entries[i])))
            
            if i == 7:
                rectangle1 = Rectangle().scale(FRAME_SCALE*0.75).next_to(queue_element2, UP, buff=0)
                bg_rec1 = BackgroundRectangle(rectangle1, color=YELLOW, stroke_width=1)
                rec_label1 = Text('c').scale(0.5).next_to(bg_rec1, ORIGIN)
                queue_element1 = VGroup(bg_rec1, rec_label1)
                self.play(FadeIn(queue_element1, shift=DOWN))

                t[1][2] = '3'
                table2 = Table(
                    table=t,
                    row_labels=[Text('vertex v'), Text('distance(v)')]
                ).scale(0.35).move_to((FRAME_CENTER+RIGHT*2.5+UP))
                self.play(ReplacementTransform(table1, table2))
            if i == 14:
                rectangle1 = Rectangle().scale(FRAME_SCALE*0.75).next_to(queue_element2, UP, buff=0)
                bg_rec1 = BackgroundRectangle(rectangle1, color=YELLOW, stroke_width=1)
                rec_label1 = Text('e').scale(0.5).next_to(bg_rec1, ORIGIN)
                queue_element1 = VGroup(bg_rec1, rec_label1)
                self.play(FadeIn(queue_element1, shift=DOWN))
          
                t[1][4] = '7'
                table1 = Table(
                    table=t,
                    row_labels=[Text('vertex v'), Text('distance(v)')]
                ).scale(0.35).move_to((FRAME_CENTER+RIGHT*2.5+UP))
                self.play(ReplacementTransform(table2, table1))
        
        self.wait(2)
        self.clear()

    def reference(self):
        title = Title("Reference").set_color(BLUE)
        text = Text("[1] Introduction to Algorithms (Second Edition)").scale(0.8).next_to(title, DOWN, buff=0.7).to_corner(LEFT)
        self.play(
            Create(title),
            Write(text)
        )
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(text)
        )
    
    def video_end(self):
        text = Text('Thanks for watching.')
        self.play(
            Write(text)
        )
        self.wait(2)

    def draw_code_all_lines_at_a_time(self, code, **kwargs):
        self.play(LaggedStart(*[
                Write(code[i]) 
                for i in range(code.__len__())
            ]),
            **kwargs
        )

    def get_remark_rectangle(
            self, 
            code, 
            line, 
            fill_opacity=0.4, 
            stroke_width=0,
            fill_color=YELLOW,
            **kwargs):
        lines = VGroup(code[2],code[1])
        w, h = getattr(lines, "width"), getattr(lines, "height")
        frame = Rectangle(width=w,height=h)

        code_line = code[1][line-1]
        line_rectangle = Rectangle(
            width=w,
            height=getattr(code[1][line-1],"height")*1.5,
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
            fill_color=fill_color,
            **kwargs
        )
        line_rectangle.set_y(code_line.get_y())
        line_rectangle.scale([1.1,1,1])
        return line_rectangle

    def change_line(self, code, rect, next_line, *args, **kwargs):
        self.play(
            Transform(
                rect,
                self.get_remark_rectangle(code, next_line),
            ),
            *args,
            **kwargs,
        )


