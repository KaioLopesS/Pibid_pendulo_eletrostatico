from manim import *
import numpy as np


class CoulombPendulum(Scene):
    def construct(self):
        self.setup_scene_parameters()
        self.show_title()
        self.setup_pendulum()
        self.introduce_fixed_charge()
        self.show_repulsion_effect() 
        self.show_complete_force_diagram_then_simplify()
        self.demonstrate_distance_effect()
        self.demonstrate_charge_product_effect() 
        self.explain_coulomb_law()

    def setup_scene_parameters(self):
        self.pivot_point = UP * 2.5
        self.pendulum_length = 2.5
        self.bob_radius = 0.2
        self.fixed_charge_radius = 0.25
        self.force_scale = 1.2 
        self.theta_equilibrium = PI / 6 

    def show_title(self):
        self.title = Tex("Pêndulo Eletrostático e a Lei de Coulomb", font_size=36)
        self.title.set_color(WHITE).set_weight(BOLD)
        self.play(Write(self.title)); self.wait(1)
        self.play(self.title.animate.to_edge(UP))

    def setup_pendulum(self):
        self.pivot_dot = Dot(self.pivot_point, color=GRAY, radius=0.08)
        pivot_label = Tex("Pivô", font_size=24).next_to(self.pivot_dot, UP, buff=0.1).set_color(WHITE) 

        self.bob_initial_pos = self.pivot_point + DOWN * self.pendulum_length

        self.bob = Circle(radius=self.bob_radius, fill_opacity=0.8, color=BLUE_C, stroke_width=2).move_to(self.bob_initial_pos)
        self.bob_center = Dot(self.bob_initial_pos, color=WHITE, radius=0.01)
        self.bob_label = MathTex("q_1", font_size=30).next_to(self.bob, DOWN, buff=0.15)

        self.string = Line(self.pivot_point, self.bob.get_center(), stroke_width=2, color=WHITE)

        self.play(Create(self.pivot_dot), Write(pivot_label))
        self.play(Create(self.string), Create(self.bob), Create(self.bob_center))
        self.play(Write(self.bob_label)); self.wait(1)

    def introduce_fixed_charge(self):
        initial_pos_q2 = self.bob_initial_pos + LEFT * 3.5
        self.fixed_charge_final_pos_value = self.bob_initial_pos + LEFT * 1.8

        self.fixed_charge = Circle(radius=self.fixed_charge_radius, fill_opacity=0.8, color=RED_C, stroke_width=2).move_to(initial_pos_q2)
        self.fixed_charge_center = Dot(initial_pos_q2, color=WHITE, radius=0.01)
        self.fixed_charge_label = MathTex("q_2", font_size=30).next_to(self.fixed_charge, DOWN, buff=0.15)
        self.plus_sign_q2 = MathTex("+", font_size=20, color=WHITE).move_to(self.fixed_charge.get_center())

        intro_text = Tex("Aproximamos uma carga fixa $q_2$ positiva...", font_size=30).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(intro_text))

        self.play(Create(self.fixed_charge), Create(self.fixed_charge_center), Write(self.plus_sign_q2), Write(self.fixed_charge_label))

        self.play(
            self.fixed_charge.animate.move_to(self.fixed_charge_final_pos_value),
            self.fixed_charge_center.animate.move_to(self.fixed_charge_final_pos_value),
            self.plus_sign_q2.animate.move_to(self.fixed_charge_final_pos_value),
            self.fixed_charge_label.animate.next_to(self.fixed_charge_final_pos_value + DOWN * self.fixed_charge_radius, DOWN, buff=0.15)
        )
        self.play(FadeOut(intro_text)); self.wait(0.5)

    def show_repulsion_effect(self):
        scene_narrative_text = Tex("O p\\^endulo ($q_1$) est\\'a inicialmente neutro.", font_size=30).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(scene_narrative_text))
        self.wait(1.5)

        contact_intro_text = Tex("Fazemos a carga $q_2$ (positiva) tocar o p\\^endulo...", font_size=30).move_to(scene_narrative_text)
        self.play(Transform(scene_narrative_text, contact_intro_text))
        self.wait(1)

        q2_resting_pos = self.fixed_charge.get_center().copy()
        q1_pos = self.bob.get_center().copy()

        contact_x_for_q2_center = q1_pos[0] - (self.bob_radius + self.fixed_charge_radius + 0.01)
        contact_pos_for_q2 = np.array([contact_x_for_q2_center, q1_pos[1], 0])

        self.play(
            self.fixed_charge.animate.move_to(contact_pos_for_q2),
            self.fixed_charge_center.animate.move_to(contact_pos_for_q2),
            self.plus_sign_q2.animate.move_to(contact_pos_for_q2),
            self.fixed_charge_label.animate.next_to(contact_pos_for_q2 + DOWN*self.fixed_charge_radius, DOWN, buff=0.15)
        )
        self.wait(0.5)

        electrization_text = Tex("...ocorre eletriza\\c{c}\\~ao por contato!", font_size=30).move_to(scene_narrative_text)
        self.play(Transform(scene_narrative_text, electrization_text))

        self.play(self.bob.animate.set_color(RED_E))
        self.plus_sign_q1 = MathTex("+", font_size=16, color=WHITE).move_to(self.bob.get_center())
        self.play(Write(self.plus_sign_q1))
        self.wait(0.5)

        self.play(
            self.fixed_charge.animate.move_to(q2_resting_pos),
            self.fixed_charge_center.animate.move_to(q2_resting_pos),
            self.plus_sign_q2.animate.move_to(q2_resting_pos),
            self.fixed_charge_label.animate.next_to(q2_resting_pos + DOWN*self.fixed_charge_radius, DOWN, buff=0.15)
        )
        self.wait(0.5)

        self.setup_pendulum_updaters()

        both_charged_text = Tex("Agora $q_1$ e $q_2$ s\\~ao ambas positivas.", font_size=30).move_to(scene_narrative_text)
        self.play(Transform(scene_narrative_text, both_charged_text))

        repulsion_text_popup = Tex("Repuls\\~ao eletrost\\'atica!", font_size=24, color=YELLOW).next_to(both_charged_text, UP, buff=0.2)
        self.play(Write(repulsion_text_popup))

        self.deflected_pos_bob = self.pivot_point + self.pendulum_length * (DOWN * np.cos(self.theta_equilibrium) + RIGHT * np.sin(self.theta_equilibrium))
        self.play(self.bob.animate.move_to(self.deflected_pos_bob), run_time=2)
        self.wait(1)

        self.play(FadeOut(scene_narrative_text), FadeOut(repulsion_text_popup))
        self.wait(0.5)

    def setup_pendulum_updaters(self):
        if self.string.updaters: self.string.clear_updaters()
        self.string.add_updater(lambda s: s.put_start_and_end_on(self.pivot_point, self.bob.get_center()))
        
        if self.bob_center.updaters: self.bob_center.clear_updaters()
        self.bob_center.add_updater(lambda d: d.move_to(self.bob.get_center()))
        
        if self.bob_label.updaters: self.bob_label.clear_updaters()
        self.bob_label.add_updater(lambda m: m.next_to(self.bob, DOWN, buff=0.15))
        
        if hasattr(self, 'plus_sign_q1') and self.plus_sign_q1:
            if self.plus_sign_q1.updaters: self.plus_sign_q1.clear_updaters()
            self.plus_sign_q1.add_updater(lambda p: p.move_to(self.bob.get_center()))

    def show_complete_force_diagram_then_simplify(self):
        dcl_title = Tex("For\\c{c}as no P\\^endulo", font_size=40).set_weight(BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(self.title, dcl_title))

        self.Fg_vec = Arrow(self.bob.get_center(), self.bob.get_center() + DOWN * self.force_scale, buff=0, color=GREEN, stroke_width=6)
        self.Fg_label = MathTex(r"\vec{F}_g", font_size=26, color=GREEN).next_to(self.Fg_vec, DOWN, buff=0.1)

        Fe_length_initial = self.force_scale * np.tan(self.theta_equilibrium)
        self.Fe_vec_diag = Arrow(self.bob.get_center(), self.bob.get_center() + RIGHT * Fe_length_initial, buff=0, color=ORANGE, stroke_width=6)
        self.Fe_label_diag = MathTex(r"\vec{F}_e", font_size=26, color=ORANGE).next_to(self.Fe_vec_diag, RIGHT, buff=0.1)

        self.T_vec = Arrow(self.bob.get_center(), self.pivot_point, buff=self.bob_radius, color=BLUE, stroke_width=6)
        self.T_label = MathTex(r"\vec{T}", font_size=26, color=BLUE).next_to(self.T_vec.get_center(), LEFT, buff=0.1)

        forces_text = Tex("Tr\\^es for\\c{c}as atuam no p\\^endulo:", font_size=30).to_edge(DOWN).shift(UP*0.5)
        self.play(Write(forces_text))
        self.play(GrowArrow(self.Fg_vec), Write(self.Fg_label)); self.wait(0.5)
        self.play(GrowArrow(self.Fe_vec_diag), Write(self.Fe_label_diag)); self.wait(0.5)
        self.play(GrowArrow(self.T_vec), Write(self.T_label)); self.wait(1.5)

        simplify_text = Tex("Focaremos na for\\c{c}a el\\'etrica ($F_e$)", font_size=30).move_to(forces_text)
        self.play(Transform(forces_text, simplify_text))
        self.play(FadeOut(self.Fg_vec), FadeOut(self.Fg_label),
                  FadeOut(self.T_vec), FadeOut(self.T_label), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(self.Fe_vec_diag), FadeOut(self.Fe_label_diag), FadeOut(forces_text))

    def setup_demo_environment(self, demo_type):
        if "distance" in demo_type: demo_title_text = r"$F_e \text{ vs. Dist\^ancia } (r)$"
        elif "charge_product" in demo_type: demo_title_text = r"$F_e \text{ vs. Produto das Cargas } (q_1q_2)$"
        else: return

        new_title = Tex(demo_title_text, font_size=40).set_weight(BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(self.title, new_title))

        self.bob_pos_at_theta_eq = getattr(self, 'deflected_pos_bob', # Use final pos from repulsion
                                           self.pivot_point + self.pendulum_length * (
                                           DOWN * np.cos(self.theta_equilibrium) + RIGHT * np.sin(self.theta_equilibrium)))
        
        self.r_at_theta_eq = np.linalg.norm(self.bob_pos_at_theta_eq - self.fixed_charge_final_pos_value)
        Fe_viz_at_theta_eq = self.force_scale * np.tan(self.theta_equilibrium)
        self.K_COULOMB_SCALED_BASE = Fe_viz_at_theta_eq * (self.r_at_theta_eq**2)

        self.current_r_tracker = ValueTracker(self.r_at_theta_eq)
        self.current_Fe_tracker = ValueTracker(Fe_viz_at_theta_eq)
        self.charge_product_factor_tracker = ValueTracker(1.0)

        # Ensure bob and fixed_charge are at their equilibrium/demo positions
        if np.linalg.norm(self.bob.get_center() - self.bob_pos_at_theta_eq) > 0.01:
            self.bob.move_to(self.bob_pos_at_theta_eq)
            if self.string.updaters: self.string.update(0)
            if self.bob_center.updaters: self.bob_center.update(0)
            if self.bob_label.updaters: self.bob_label.update(0)
            if hasattr(self, 'plus_sign_q1') and self.plus_sign_q1 and self.plus_sign_q1.updaters: self.plus_sign_q1.update(0)
        
        if np.linalg.norm(self.fixed_charge.get_center() - self.fixed_charge_final_pos_value) > 0.01:
            self.fixed_charge.move_to(self.fixed_charge_final_pos_value)
            if self.fixed_charge_center.updaters: self.fixed_charge_center.update(0)
            if self.plus_sign_q2.updaters: self.plus_sign_q2.update(0)
            if self.fixed_charge_label.updaters: self.fixed_charge_label.update(0)

        # Clear ALL potentially conflicting updaters
        elements_to_clear_all_updaters = [
            self.bob, self.string, self.bob_center, self.bob_label, 
            self.fixed_charge, self.fixed_charge_center, self.fixed_charge_label, self.plus_sign_q2,
            self.current_r_tracker # if it had updaters from distance demo
        ]
        if hasattr(self, 'plus_sign_q1') and self.plus_sign_q1:
            elements_to_clear_all_updaters.append(self.plus_sign_q1)
        
        for mobj in elements_to_clear_all_updaters:
            if mobj and hasattr(mobj, 'clear_updaters'): mobj.clear_updaters()
        
        if hasattr(self, 'bob_physics_updater_obj'):
            self.bob_physics_updater_obj.clear_updaters()
            if self.bob_physics_updater_obj in self.mobjects: self.remove(self.bob_physics_updater_obj)
            delattr(self, 'bob_physics_updater_obj')
        if hasattr(self, 'charge_product_specific_physics_updater'): # from previous charge demo run
            self.charge_product_specific_physics_updater.clear_updaters()
            if self.charge_product_specific_physics_updater in self.mobjects: self.remove(self.charge_product_specific_physics_updater)
            delattr(self, 'charge_product_specific_physics_updater')


        self.setup_pendulum_updaters() # For string, bob_center, bob_label relative to bob's (now static) position
        
        self.fixed_charge_center.add_updater(lambda m: m.move_to(self.fixed_charge.get_center()))
        self.fixed_charge_label.add_updater(lambda m: m.next_to(self.fixed_charge, DOWN, buff=0.15))

        self.original_plus_q1_height = self.plus_sign_q1.height if hasattr(self, 'plus_sign_q1') and self.plus_sign_q1 else 0.2
        self.original_plus_q2_height = self.plus_sign_q2.height if self.plus_sign_q2 else 0.2

        if "distance" in demo_type:
            self.parameter_tracker = ValueTracker(self.fixed_charge.get_center()[0]) 
            self.charge_product_factor_tracker.set_value(1.0) 

            initial_y_q2 = self.fixed_charge_final_pos_value[1]
            self.fixed_charge.add_updater(lambda m: m.move_to([self.parameter_tracker.get_value(), initial_y_q2, 0]))
            
            # plus_sign_q1 already handled by setup_pendulum_updaters
            self.plus_sign_q2.add_updater(lambda p: p.move_to(self.fixed_charge.get_center()))
            
            self.setup_bob_and_Fe_physics_updater() # This updater MOVES THE BOB

        elif "charge_product" in demo_type:
            self.parameter_tracker = self.charge_product_factor_tracker
            self.current_r_tracker.set_value(self.r_at_theta_eq) # r is fixed

            min_scale_factor = 0.25 
            if hasattr(self, 'plus_sign_q1') and self.plus_sign_q1:
                # setup_pendulum_updaters already set pos, now add height scaling
                self.plus_sign_q1.add_updater(lambda p: p.set_height(
                    self.original_plus_q1_height * np.sqrt(max(min_scale_factor, self.charge_product_factor_tracker.get_value()))
                ))
            self.plus_sign_q2.add_updater(lambda p: p.move_to(self.fixed_charge.get_center()).set_height(
                self.original_plus_q2_height * np.sqrt(max(min_scale_factor, self.charge_product_factor_tracker.get_value()))
            ))
            
            self.charge_product_specific_physics_updater = Mobject()
            def charge_product_physics_func_local(mobj_updater):
                q1q2_f = self.charge_product_factor_tracker.get_value()
                Fe_calc = (self.K_COULOMB_SCALED_BASE * q1q2_f) / (self.r_at_theta_eq**2)
                max_Fe_viz = self.force_scale * np.tan(PI * 0.48) 
                self.current_Fe_tracker.set_value(min(Fe_calc, max_Fe_viz))
                # self.current_r_tracker is already set to fixed r_at_theta_eq and has no updater

            self.charge_product_specific_physics_updater.add_updater(charge_product_physics_func_local)
            self.add(self.charge_product_specific_physics_updater)
            # Bob does NOT move, so no bob_physics_updater_obj needed here

    def create_dynamic_visuals(self, demo_type):
        self.dist_line_dyn = DashedLine(self.bob.get_center(), self.fixed_charge.get_center(), color=YELLOW_D, stroke_width=3)
        self.dist_label_r_on_line = MathTex("r", font_size=28, color=ORANGE)
        if self.dist_line_dyn.updaters: self.dist_line_dyn.clear_updaters()
        self.dist_line_dyn.add_updater(lambda l: l.put_start_and_end_on(self.bob.get_center(), self.fixed_charge.get_center()))
        if self.dist_label_r_on_line.updaters: self.dist_label_r_on_line.clear_updaters()
        self.dist_label_r_on_line.add_updater(lambda m: m.next_to(self.dist_line_dyn.get_center(), UP, buff=0.1))

        if not (self.dist_line_dyn in self.mobjects): self.add(self.dist_line_dyn)
        if not (self.dist_label_r_on_line in self.mobjects): self.add(self.dist_label_r_on_line)

        prop_color_map_base = {"F_e": ORANGE}
        if "distance" in demo_type:
            prop_text_str = r"F_e \propto \frac{1}{r^2}"; prop_color_map = {"r^2": YELLOW_D}
        elif "charge_product" in demo_type:
            prop_text_str = r"F_e \propto q_1 q_2"; prop_color_map = {"q_1 q_2": BLUE_D}

        prop_text = MathTex(prop_text_str, font_size=36).set_color_by_tex_to_color_map({**prop_color_map_base, **prop_color_map})
        prop_text.to_corner(UL, buff=0.5).shift(DOWN * (self.title.height + 0.4))
        self.play(Write(prop_text)); self.active_proportionality_text = prop_text

        r_label_text = MathTex("r =", font_size=28, color=YELLOW_D)
        self.r_value_display = DecimalNumber(self.current_r_tracker.get_value(), num_decimal_places=2, font_size=28, color=YELLOW_D)
        if self.r_value_display.updaters: self.r_value_display.clear_updaters()
        self.r_value_display.add_updater(lambda d: d.set_value(self.current_r_tracker.get_value()))

        Fe_label_text = MathTex("F_e =", font_size=28, color=ORANGE)
        self.Fe_value_display = DecimalNumber(self.current_Fe_tracker.get_value(), num_decimal_places=2, font_size=28, color=ORANGE)
        if self.Fe_value_display.updaters: self.Fe_value_display.clear_updaters()
        self.Fe_value_display.add_updater(lambda d: d.set_value(self.current_Fe_tracker.get_value()))

        data_vgroup_list = [VGroup(r_label_text, self.r_value_display).arrange(RIGHT, buff=SMALL_BUFF)]

        if "distance" in demo_type:
            r_sq_label = MathTex("r^2 =", font_size=28, color=YELLOW_D)
            self.r_sq_value_display = DecimalNumber(self.current_r_tracker.get_value()**2, num_decimal_places=2, font_size=28, color=YELLOW_D)
            if self.r_sq_value_display.updaters: self.r_sq_value_display.clear_updaters()
            self.r_sq_value_display.add_updater(lambda d: d.set_value(max(0.001, self.current_r_tracker.get_value()**2)))
            data_vgroup_list.append(VGroup(r_sq_label, self.r_sq_value_display).arrange(RIGHT, buff=SMALL_BUFF))
        elif "charge_product" in demo_type:
            q_prod_label = MathTex(r"(q_1q_2)_{\text{rel}} =", font_size=28, color=BLUE_D)
            self.q_prod_display = DecimalNumber(self.charge_product_factor_tracker.get_value(), num_decimal_places=2, font_size=28, color=BLUE_D)
            if self.q_prod_display.updaters: self.q_prod_display.clear_updaters()
            self.q_prod_display.add_updater(lambda d: d.set_value(self.charge_product_factor_tracker.get_value()))
            data_vgroup_list.append(VGroup(q_prod_label, self.q_prod_display).arrange(RIGHT, buff=SMALL_BUFF))

        data_vgroup_list.append(VGroup(Fe_label_text, self.Fe_value_display).arrange(RIGHT, buff=SMALL_BUFF))

        self.numerical_data_group = VGroup(*data_vgroup_list).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.numerical_data_group.next_to(prop_text, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(self.numerical_data_group))

        self.dynamic_Fe_vec = Arrow(self.bob.get_center(), self.bob.get_center() + RIGHT*self.current_Fe_tracker.get_value(), stroke_width=6, color=ORANGE, buff=0)
        self.dynamic_Fe_label = MathTex(r"\vec{F}_e", font_size=26, color=ORANGE)
        if not (self.dynamic_Fe_vec in self.mobjects): self.add(self.dynamic_Fe_vec)
        if not (self.dynamic_Fe_label in self.mobjects): self.add(self.dynamic_Fe_label)

        self.dynamic_Fe_elements_updater_obj = Mobject()
        def dynamic_Fe_updater_func(mobj):
            Fe_mag_visual = self.current_Fe_tracker.get_value()
            current_bob_center = self.bob.get_center() 
            self.dynamic_Fe_vec.put_start_and_end_on(current_bob_center, current_bob_center + RIGHT * Fe_mag_visual)
            self.dynamic_Fe_label.next_to(self.dynamic_Fe_vec, RIGHT, buff=0.1)

        if self.dynamic_Fe_elements_updater_obj.updaters: self.dynamic_Fe_elements_updater_obj.clear_updaters()
        self.dynamic_Fe_elements_updater_obj.add_updater(dynamic_Fe_updater_func)
        if not (self.dynamic_Fe_elements_updater_obj in self.mobjects): self.add(self.dynamic_Fe_elements_updater_obj)

    def setup_bob_and_Fe_physics_updater(self):
        self.bob_physics_updater_obj = Mobject() 

        def physics_updater_func_local(mobj):
            bob_center = self.bob.get_center()
            fixed_charge_center = self.fixed_charge.get_center()
            r_val = np.linalg.norm(bob_center - fixed_charge_center)
            r_val = max(r_val, 0.1)
            self.current_r_tracker.set_value(r_val) 

            q1q2_f = self.charge_product_factor_tracker.get_value() 
            Fe_calc = (self.K_COULOMB_SCALED_BASE * q1q2_f) / (r_val**2)
            max_Fe_viz = self.force_scale * np.tan(PI * 0.48)
            Fe_display_val = min(Fe_calc, max_Fe_viz)
            self.current_Fe_tracker.set_value(Fe_display_val)

            target_theta = np.arctan(Fe_display_val / self.force_scale) if self.force_scale != 0 else (PI/2 if Fe_display_val > 0 else 0)
            new_bob_pos = self.pivot_point + self.pendulum_length * (DOWN * np.cos(target_theta) + RIGHT * np.sin(target_theta))
            self.bob.move_to(new_bob_pos) 

        if self.bob_physics_updater_obj.updaters: self.bob_physics_updater_obj.clear_updaters()
        self.bob_physics_updater_obj.add_updater(physics_updater_func_local)
        if not (self.bob_physics_updater_obj in self.mobjects): self.add(self.bob_physics_updater_obj)

    def create_graph_for_distance(self): 
        x_axis_label_str = r"$r$"
        r_min_practical = self.bob_radius + self.fixed_charge_radius + 0.1 
        r_max_practical = 4.0 
        x_min_graph, x_max_graph = max(0.2,r_min_practical), r_max_practical
        max_Fe_viz_for_graph = self.force_scale * np.tan(PI*0.48) * 1.2 
        plot_function = lambda x_plot: (self.K_COULOMB_SCALED_BASE * 1.0) / (max(0.01, x_plot**2)) 

        self.active_axes = Axes(
            x_range=[x_min_graph, x_max_graph, (x_max_graph - x_min_graph) / 5], 
            y_range=[0, max_Fe_viz_for_graph, max_Fe_viz_for_graph / 4], 
            x_length=4.0, y_length=2.5, 
            axis_config={"include_numbers": True, "font_size": 18, 
                         "decimal_number_config": {"num_decimal_places": 1}, "color": LIGHT_GRAY},
            tips=False
        ).to_corner(UR, buff=0.3).scale(0.7) 
        
        x_label_obj = self.active_axes.get_x_axis_label(Tex(x_axis_label_str, font_size=20), edge=RIGHT, direction=RIGHT, buff=0.1)
        y_label_obj = self.active_axes.get_y_axis_label(Tex("$F_e$", font_size=20).set_color(ORANGE), edge=UP, direction=UP, buff=0.1)
        graph_plot_obj = self.active_axes.plot(plot_function, 
                                               x_range=[self.active_axes.x_range[0], self.active_axes.x_range[1]], 
                                               color=ORANGE, use_smoothing=True) 
        self.moving_dot_on_graph = Dot(color=ORANGE, radius=0.05) 
        
        def update_graph_dot_func_local(dot):
            x_val = self.current_r_tracker.get_value()
            y_val = self.current_Fe_tracker.get_value() 
            ax = self.active_axes
            if ax.x_range[0] <= x_val <= ax.x_range[1] and ax.y_range[0] <= y_val <= ax.y_range[1]:
                dot.move_to(ax.c2p(x_val, y_val)).set_opacity(1)
            else: 
                dot.set_opacity(0)
        
        if self.moving_dot_on_graph.updaters: self.moving_dot_on_graph.clear_updaters()
        self.moving_dot_on_graph.add_updater(update_graph_dot_func_local)
        
        self.play(Create(self.active_axes), Write(x_label_obj), Write(y_label_obj))
        self.play(Create(graph_plot_obj)); self.play(Create(self.moving_dot_on_graph)); self.wait(1)
        self.current_graph_elements = VGroup(self.active_axes, x_label_obj, y_label_obj, graph_plot_obj, self.moving_dot_on_graph)

        initial_q2_x = self.fixed_charge_final_pos_value[0]
        final_q2_x_close = self.bob_pos_at_theta_eq[0] - (self.bob_radius + self.fixed_charge_radius + 0.3)
        final_q2_x_far = initial_q2_x - 1.5
        
        distance_narrative = Tex("Variando a dist\\^ancia $r$ entre $q_1$ e $q_2$...", font_size=24).to_edge(DOWN)
        self.play(Write(distance_narrative))

        self.play(self.parameter_tracker.animate.set_value(final_q2_x_close), run_time=3)
        self.wait(1)
        self.play(self.parameter_tracker.animate.set_value(final_q2_x_far), run_time=4)
        self.wait(1)
        self.play(self.parameter_tracker.animate.set_value(initial_q2_x), run_time=3)
        self.wait(1)
        self.play(FadeOut(distance_narrative))

    def demonstrate_distance_effect(self):
        self.setup_demo_environment("distance")
        self.create_dynamic_visuals("distance")
        self.create_graph_for_distance() 
       
        if hasattr(self, 'current_graph_elements'):
            self.play(FadeOut(self.current_graph_elements))
            if hasattr(self, 'moving_dot_on_graph') and self.moving_dot_on_graph: 
                 self.moving_dot_on_graph.clear_updaters()
                 if self.moving_dot_on_graph in self.mobjects: self.remove(self.moving_dot_on_graph)
            delattr(self, 'current_graph_elements') 

        self.cleanup_demo_visuals("distance")

    def demonstrate_charge_product_effect(self):
        self.setup_demo_environment("charge_product") 
        self.create_dynamic_visuals("charge_product") 

        q_factor_text = Tex("Variando o produto das cargas $(q_1q_2)$...", font_size=24).to_edge(DOWN)
        self.play(Write(q_factor_text))
        self.wait(1)

        self.play(
            self.charge_product_factor_tracker.animate.set_value(2.5), 
            run_time=3
        )
        self.wait(1)
        self.play(
            self.charge_product_factor_tracker.animate.set_value(0.2),
            run_time=3.5
        )
        self.wait(1)
        self.play(
            self.charge_product_factor_tracker.animate.set_value(1.0), 
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(q_factor_text))

        self.cleanup_demo_visuals("charge_product")

    def cleanup_demo_visuals(self, demo_type):
        mobjects_to_fade = []
        if hasattr(self, 'active_proportionality_text') and self.active_proportionality_text: mobjects_to_fade.append(self.active_proportionality_text)
        if hasattr(self, 'numerical_data_group') and self.numerical_data_group: mobjects_to_fade.append(self.numerical_data_group)
        
        if hasattr(self, 'dist_line_dyn') and self.dist_line_dyn:
             self.dist_line_dyn.clear_updaters(); mobjects_to_fade.append(self.dist_line_dyn)
        if hasattr(self, 'dist_label_r_on_line') and self.dist_label_r_on_line:
             self.dist_label_r_on_line.clear_updaters(); mobjects_to_fade.append(self.dist_label_r_on_line)

        if hasattr(self, 'dynamic_Fe_vec') and self.dynamic_Fe_vec: mobjects_to_fade.append(self.dynamic_Fe_vec)
        if hasattr(self, 'dynamic_Fe_label') and self.dynamic_Fe_label: mobjects_to_fade.append(self.dynamic_Fe_label)
        
        mobjects_to_fade = [m for m in mobjects_to_fade if m and m in self.mobjects]
        if mobjects_to_fade: self.play(*[FadeOut(elem) for elem in mobjects_to_fade])
        
        if hasattr(self, 'bob_physics_updater_obj'):
            self.bob_physics_updater_obj.clear_updaters()
            if self.bob_physics_updater_obj in self.mobjects: self.remove(self.bob_physics_updater_obj)
            delattr(self, 'bob_physics_updater_obj')

        if hasattr(self, 'charge_product_specific_physics_updater'): 
            self.charge_product_specific_physics_updater.clear_updaters()
            if self.charge_product_specific_physics_updater in self.mobjects: self.remove(self.charge_product_specific_physics_updater)
            delattr(self, 'charge_product_specific_physics_updater')

        if hasattr(self, 'dynamic_Fe_elements_updater_obj'):
            self.dynamic_Fe_elements_updater_obj.clear_updaters()
            if self.dynamic_Fe_elements_updater_obj in self.mobjects: self.remove(self.dynamic_Fe_elements_updater_obj)
    
        elements_to_clear_demo_updaters = [self.fixed_charge]
        if hasattr(self, 'plus_sign_q1') and self.plus_sign_q1: elements_to_clear_demo_updaters.append(self.plus_sign_q1)
        if self.plus_sign_q2: elements_to_clear_demo_updaters.append(self.plus_sign_q2)
        
        for mobj in elements_to_clear_demo_updaters:
            if mobj and hasattr(mobj, 'clear_updaters'): mobj.clear_updaters()

        if hasattr(self, 'plus_sign_q1') and self.plus_sign_q1 and hasattr(self, 'original_plus_q1_height'):
            self.plus_sign_q1.set_height(self.original_plus_q1_height)
        if self.plus_sign_q2 and hasattr(self, 'original_plus_q2_height'):
            self.plus_sign_q2.set_height(self.original_plus_q2_height)
        self.setup_pendulum_updaters() 
        
        if hasattr(self.fixed_charge_center, 'add_updater'): self.fixed_charge_center.add_updater(lambda m: m.move_to(self.fixed_charge.get_center()))
        if hasattr(self.fixed_charge_label, 'add_updater'): self.fixed_charge_label.add_updater(lambda m: m.next_to(self.fixed_charge, DOWN, buff=0.15))
        if hasattr(self.plus_sign_q2, 'add_updater'): self.plus_sign_q2.add_updater(lambda p: p.move_to(self.fixed_charge.get_center()))
        
        if hasattr(self, 'charge_product_factor_tracker'): self.charge_product_factor_tracker.set_value(1.0)

        target_q2_pos = self.fixed_charge_final_pos_value
        if np.linalg.norm(self.fixed_charge.get_center() - target_q2_pos) > 0.01:
            self.play(self.fixed_charge.animate.move_to(target_q2_pos), run_time=0.5)
        
        final_bob_pos_after_demo = self.bob_pos_at_theta_eq 
        if np.linalg.norm(self.bob.get_center() - final_bob_pos_after_demo) > 0.01:
            self.play(self.bob.animate.move_to(final_bob_pos_after_demo), run_time=1)
        
        self.wait(0.5)

    def explain_coulomb_law(self):
        coulomb_title = Tex("Lei de Coulomb", font_size=40).set_weight(BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(self.title, coulomb_title))

        bob_final_pos = self.bob_pos_at_theta_eq 
        if np.linalg.norm(self.bob.get_center() - bob_final_pos) > 0.01:
            self.play(self.bob.animate.move_to(bob_final_pos))
        
        fixed_charge_pos = self.fixed_charge_final_pos_value
        if np.linalg.norm(self.fixed_charge.get_center() - fixed_charge_pos) > 0.01:
            self.play(self.fixed_charge.animate.move_to(fixed_charge_pos))
        self.wait(0.2) 

        static_Fe_magnitude = self.force_scale * np.tan(self.theta_equilibrium)
        final_Fe_arrow = Arrow(self.bob.get_center(), self.bob.get_center() + RIGHT * static_Fe_magnitude, buff=0, color=ORANGE, stroke_width=6)
        final_Fe_label = MathTex(r"\vec{F}_e", font_size=26, color=ORANGE).next_to(final_Fe_arrow, RIGHT, buff=0.1)
        
        final_dist_line = DashedLine(self.bob.get_center(), self.fixed_charge.get_center(), color=YELLOW_D, stroke_width=3)
        final_dist_label = MathTex("r", font_size=28, color=ORANGE).next_to(final_dist_line.get_center(), UP, buff=0.1)

        self.play(AnimationGroup(
            Create(final_Fe_arrow), Write(final_Fe_label),
            Create(final_dist_line), Write(final_dist_label),
            lag_ratio=0.5
        ))
        self.wait(1)

        summary_text = Tex(r"Das observa\c{c}\~oes:", font_size=30, color=WHITE).to_corner(UL, buff=0.5).shift(DOWN * (self.title.height + 0.5))
        self.play(Write(summary_text))
        
        props = VGroup(
            MathTex(r"F_e \propto q_1 q_2", font_size=30, tex_to_color_map={"q_1 q_2": BLUE_D, "F_e": ORANGE}),
            MathTex(r"F_e \propto \frac{1}{r^2}", font_size=30, tex_to_color_map={"r^2": YELLOW_D, "F_e": ORANGE})
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(summary_text, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(props[0])); self.wait(1)
        self.play(Write(props[1])); self.wait(1)
        
        prop_combined = MathTex(r"F_e \propto \frac{q_1 q_2}{r^2}", font_size=36, color=GOLD).next_to(props, DOWN, buff=0.4, aligned_edge=LEFT) 
        self.play(Write(prop_combined)); self.wait(1)
        
        coulomb_law_final_formula = MathTex(r"F_e = k \frac{|q_1 q_2|}{r^2}", font_size=38, color=GOLD)
        k_explanation_final = Tex(r"onde $k$ é a constante de Coulomb ($k \approx 8.99 \times 10^9 \, \text{N}\cdot\text{m}^2/\text{C}^2$)", font_size=22, color=WHITE)
        
        final_law_group = VGroup(coulomb_law_final_formula, k_explanation_final).arrange(DOWN, buff=0.3)
        final_law_group.to_edge(DOWN, buff=1.0)

        law_box = SurroundingRectangle(coulomb_law_final_formula, buff=0.2, color=GOLD, stroke_width=2)
        
        prop_combined_copy = prop_combined.copy()
        self.play(
            ReplacementTransform(prop_combined_copy, coulomb_law_final_formula.move_to(final_law_group[0])), 
            Create(law_box)
        )
        if prop_combined in self.mobjects: self.remove(prop_combined) 
        self.add(coulomb_law_final_formula)

        self.play(Write(k_explanation_final.move_to(final_law_group[1]))); self.wait(5)

        self.play(FadeOut(final_Fe_arrow), FadeOut(final_Fe_label), FadeOut(final_dist_line), FadeOut(final_dist_label))
        self.wait(1)
        self.play(FadeOut(summary_text), FadeOut(props), FadeOut(prop_combined_copy), FadeOut(final_law_group), FadeOut(law_box))
        self.wait(2) 