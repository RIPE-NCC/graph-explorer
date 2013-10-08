%include templates/snippet.errors errors=errors
% if 'query' in globals():
    % if not query:
        % include templates/snippet.info msg='Empty query.  Nothing to display.'
    % end

    % if query and not errors:
        <script language="javascript">
        tags = {{!list(tags)}};
        colormap = create_colormap(tags);
        count_interval = {{preferences.count_interval}};
        $("#tag_legend").html(list_tags_in_graph_name_order({{!list(tags)}}));
        $("#patterns").html(generate_pattern_display({{!list(query['patterns'])}}));
        $("#group_by").html(generate_pattern_display({{!list(query['group_by'])}}));
        $("#avg_by").html(generate_pattern_display({{!list(query['avg_by'])}}) || 'none');
        $("#sum_by").html(generate_pattern_display({{!list(query['sum_by'])}}) || 'none');
        </script>
            <dl class="dl-horizontal span6" style="margin-top: 0px;">
                <dt>Statement</dt><dd>{{query['statement']}}</dd>
                <dt>Limit</dt><dd>{{query['limit_targets']}}</dd>
                <dt>Patterns<dt><dd><span id="patterns"></span></dd>
                <dt>Group by</dt><dd><span id="group_by"></span></dd>
                <dt>Aggregation</dt><dd>avg by <span id="avg_by"></span>, sum by <span id="sum_by"></span></dd>
                <dt>X-axis</dt><dd>from {{query['from']}}, to {{query['to']}}</dd>
                <dt>Y-axis</dt><dd>min {{query['min']}}, max {{query['max']}}</dd>
                % if query['avg_over']:
                    % avg_over_display = {'s': 'seconds', 'M': 'minutes', 'h': 'hours', 'd': 'days', 'w': 'weeks', 'mo': 'months'}
                    <dt>Avg over</dt><dd>{{query['avg_over'][0]}} {{avg_over_display[query['avg_over'][1]]}}</dd>
                % end
            </dl>
            <dl class="dl-horizontal span6">
                <dt>Targets matching</dt><dd>{{len_targets_matching}}/{{len_targets_all}}</dd>
                <dt>Graphs matching</dt><dd>{{len_graphs_matching}}/{{len_graphs_all}}</dd>
                <dt>Graphs from matching targets</dt><dd>{{len_graphs_targets_matching}}</dd>
                <dt>Total graphs</dt><dd>{{len_graphs_matching_all}}</dd>
                <dt>Tag legend</dt><dd><span id="tag_legend"></span></dd>
            </dl>
        <div class="span12">
        % for (k,v) in graphs:
            % include templates/snippet.graph config=config, graph_key=k, graph_data=v, preferences=preferences
        % end
        <!-- approximation of get_inspect_url(data, name) that works as long as list mode doesn't support sum by (or other kind of N metrics in 1 target) -->
        % for target_id in targets_list.iterkeys():
            <a href="/inspect/{{targets_list[target_id]['id']}}">{{target_id}}</a></br>
        % end
        </div>
    % end
% else:
    % include templates/snippet.info msg='No query processed.  Nothing to display.'
% end
