import os
import json
import argparse
from TStar.interface_grounding import TStarUniversalGrounder
from TStar.interface_heuristic import HeuristicInterface
from TStar.TStarFramework import TStarFramework, initialize_heuristic
from LVHaystackBench.run_TStar_onDataset import get_TStar_search_results

def process_single_entry(video_path, question, options, gt_answer, config):
    """Process a single entry with specified video path, question, and options."""
    
    # Create a mock data item similar to those in the dataset
    data_item = {
        "video_path": video_path,
        "question": question,
        "options": options,
    }

    # Initialize Search tools
    grounder = TStarUniversalGrounder(model_name=config['grounder'])
    heuristic = initialize_heuristic(heuristic_type=config['heuristic'])

    # Get the result for this single data item
    result = get_TStar_search_results(
        args=argparse.Namespace(**config),  # Convert config dictionary to Namespace for compatibility
        data_item=data_item,
        grounder=grounder,
        heurisiticFuncion=heuristic
    )

    # Print the results
    print(f"Processed Video Path: {video_path}")
    print("Results:")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run TStar on a single video with a specific question")
    
    # Add arguments for video path, question, and options
    parser.add_argument("--video_path", type=str, required=True, help="Path to the video file")
    parser.add_argument("--question", type=str, required=True, help="Question to ask about the video")
    parser.add_argument("--options", type=str, required=True, help="Multiple choice options (e.g., 'A) Red\\nB) Black\\nC) Blue\\nD) White')")
    
    # Add optional configuration parameters with defaults
    parser.add_argument("--grounder", type=str, default="gpt-4o", help="Model name for the grounder")
    parser.add_argument("--heuristic", type=str, default="owl-vit", help="Heuristic type")
    parser.add_argument("--search_nframes", type=int, default=8, help="Number of frames to search")
    parser.add_argument("--grid_rows", type=int, default=4, help="Number of grid rows")
    parser.add_argument("--grid_cols", type=int, default=4, help="Number of grid columns")
    parser.add_argument("--confidence_threshold", type=float, default=0.7, help="Confidence threshold")
    parser.add_argument("--search_budget", type=float, default=1.0, help="Search budget")
    parser.add_argument("--output_dir", type=str, default="./results/frame_search", help="Output directory")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create config dictionary from arguments
    config = {
        'grounder': args.grounder,
        'heuristic': args.heuristic,
        'search_nframes': args.search_nframes,
        'grid_rows': args.grid_rows,
        'grid_cols': args.grid_cols,
        'confidence_threshold': args.confidence_threshold,
        'search_budget': args.search_budget,
        'output_dir': args.output_dir,
    }
    
    # Call the process function with the provided arguments
    process_single_entry(args.video_path, args.question, args.options, None, config)
